from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from .models import BlogPost, BlogComment
from django.template import loader
from core.models import CategoryModel
from django.core.paginator import Paginator
from formation.models import Formation
from ebook.models import EbookModel
from django.db.models import Count
from django.db.models import Q
from django.contrib import messages
from profil.models import UserProfilModel
from django.contrib.auth.decorators import login_required

def index(request: WSGIRequest):
    category_id = request.GET.get("category_id")
    search_input = request.GET.get("search_input")
    post_category_list = CategoryModel.objects.order_by("-created_at")
    context = {}

    if search_input is not None:
        latest_post_list = BlogPost.objects.filter(Q(title__icontains=search_input) | Q(subtitle__icontains=search_input), published=True)
    elif category_id is not None:
        latest_post_list = BlogPost.objects.filter(category=category_id, published=True)
        target_category = [cat for cat in post_category_list if cat.id == int(category_id)]
        if len(target_category) != 0:
            context["category"] = target_category[0]
    else:
        latest_post_list = BlogPost.objects.filter(published=True)
        
    paginator = Paginator(latest_post_list, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number if page_number is not None else 1)
    
    formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
        video_count=Count('formationvideo__id'))[:2]
    
    EbookModelWithSales = EbookModel.objects.annotate(
        sales_count=Count('saleebook__id')
    )
    if category_id is not None:
        top_3_ebooks = EbookModelWithSales.filter(category=category_id, published=True).order_by('-sales_count')[:3]
        if len(top_3_ebooks) == 0:
            top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]
    else:
        top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]


    context["ebooks"] = top_3_ebooks
    context["formations"] = formation_list
    context["page_obj"] = page_obj
    context["selected_tab"] = "blog"
    context["search_input"] = search_input if search_input is not None else ""
    context["title"] = "Blog | site vie de réussite"
    context["post_category_list"] = post_category_list
    return render(request, "blog/index.html", context)


def detail(request, post_id):
    target_post = BlogPost.objects.get(id=post_id)
    post_comments = BlogComment.objects.filter(post=target_post, reply_of__isnull=True).order_by("-created_at")[:5]
    related_post_category = BlogPost.objects.filter(category=target_post.category.id, published=True).exclude(id=target_post.id)[:20]
    formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
        video_count=Count('formationvideo__id'))[:2]
    EbookModelWithSales = EbookModel.objects.annotate(
        sales_count=Count('saleebook__id')
    )
    top_3_ebooks = EbookModelWithSales.filter(category=target_post.category.id, published=True).order_by('-sales_count')[:3]
    if len(top_3_ebooks) == 0:
        top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]

    context = {
        "post": target_post,
        "ebooks": top_3_ebooks,
        "title": target_post.title,
        "selected_tab": "blog",
        "formations": formation_list,
        "post_comments": post_comments,
        "related_post_category": related_post_category,
    }
    # print("************************============================= "+str(post_id))
    # print("************************============================= "+str(post_id))
    return render(request, "blog/details.html", context)

@login_required
def comment(request: WSGIRequest, post_id: int):
    if request.POST:
        content: str = request.POST.get("content")
        post = BlogPost.objects.get(id=post_id)
        print("le profil de l'utilisateur: ")
        print(request.session.load())
        user_profil_session = request.session.get("user_profile")
        print(user_profil_session)
        user_profil_id = user_profil_session.get("id")
        user_profil = UserProfilModel.objects.get(id=user_profil_id)
        print(user_profil)

        new_comment = BlogComment.objects.create(content=content, post=post, author=user_profil)
        new_comment.save()
        messages.success(request, "Votre commentaire a été ajouté avec succès")
        return redirect(f"/blog/{post_id}")
    else:
        return redirect(f"/blog/{post_id}")


@login_required
def reply(request: WSGIRequest, comment_id: int):
    if request.POST:
        content: str = request.POST.get("reply_content")
        comment = BlogComment.objects.get(id=comment_id)
        user_profil = UserProfilModel.objects.get(id=request.session.get("user_profile").get("id"))
        new_comment = BlogComment.objects.create(content=content, post=comment.post, author=user_profil, reply_of=comment)
        new_comment.save()
        # comment.reply_of
        # comment.save()
        messages.success(request, "Votre reponse a été ajouté avec succès")
        return redirect(f"/blog/{comment.post.id}")
    else:
        return redirect(f"/blog/{comment.post.id}")


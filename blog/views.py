from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import BlogPost, BlogComment
from django.template import loader
from django.urls import reverse
from core.models import CategoryModel
from django.core.paginator import Paginator
from formation.models import Formation
from ebook.models import EbookModel
from django.db.models import Count

def index(request: WSGIRequest):
    # contact_list = Contact.objects.all()
    # paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # return render(request, "list.html", {"page_obj": page_obj})

    category_id = request.GET.get("category_id")
    post_category_list = CategoryModel.objects.order_by("-created_at")
    context = {}
    if category_id is not None:
        latest_post_list = BlogPost.objects.filter(category=category_id)
        target_category = [cat for cat in post_category_list if cat.id == int(category_id)]
        if len(target_category) != 0:
            context["category"] = target_category[0]
    else:
        latest_post_list = BlogPost.objects.all()
        
    paginator = Paginator(latest_post_list, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number if page_number is not None else 1)
    
    formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
        video_count=Count('formationvideo__id'))[:2]
    
    EbookModelWithSales = EbookModel.objects.annotate(
        sales_count=Count('saleebook__id')
    )
    if category_id is not None:
        top_3_ebooks = EbookModelWithSales.filter(category=category_id).order_by('-sales_count')[:3]
        if len(top_3_ebooks) == 0:
            top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]
    else:
        top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]


    context["ebooks"] = top_3_ebooks
    context["formations"] = formation_list
    context["page_obj"] = page_obj
    context["post_category_list"] = post_category_list
    return render(request, "blog/index.html", context)

def detail(request, post_id):
    target_post = BlogPost.objects.get(id=post_id)
    related_post_category = BlogPost.objects.filter(category=target_post.category.id).exclude(id=target_post.id)[:20]
    #     related_ebook_category = EbookModel.objects.filter(category=target_ebook.category.id).exclude(id=target_ebook.id)[:4]
    # if len(related_ebook_category) == 0:
    #     related_ebook_category = EbookModel.objects.all().order_by("-created_at").exclude(id=target_ebook.id)[:4]
    formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
        video_count=Count('formationvideo__id'))[:2]
    
    EbookModelWithSales = EbookModel.objects.annotate(
        sales_count=Count('saleebook__id')
    )
    top_3_ebooks = EbookModelWithSales.filter(category=target_post.category.id).order_by('-sales_count')[:3]
    if len(top_3_ebooks) == 0:
        top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]

    context = {
        "post": target_post,
        "ebooks": top_3_ebooks,
        "formations": formation_list,
        "related_post_category": related_post_category,
    }
    return render(request, "blog/details.html", context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)



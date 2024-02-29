from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from core.models import CategoryModel
from django.core.paginator import Paginator
from formation.models import Formation
from ebook.models import EbookModel
from blog.models import BlogPost
from event.models import EventModel
from django.db.models import Count

def index(request: WSGIRequest):
    category_id = request.GET.get("category_id")
    event_category_list = CategoryModel.objects.order_by("-created_at")
    context = {}
    if category_id is not None:
        latest_event_list = EventModel.objects.filter(category=category_id, published=True)
        target_category = [cat for cat in event_category_list if cat.id == int(category_id)]
        if len(target_category) != 0:
            context["category"] = target_category[0]
    else:
        latest_event_list = EventModel.objects.filter(published=True)
        
    paginator = Paginator(latest_event_list, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number if page_number is not None else 1)
    
    # formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
    #     video_count=Count('formationvideo__id'))[:2]
    
    # EbookModelWithSales = EbookModel.objects.annotate(
    #     sales_count=Count('saleebook__id')
    # )
    # if category_id is not None:
    #     top_3_ebooks = EbookModelWithSales.filter(category=category_id).order_by('-sales_count')[:3]
    #     if len(top_3_ebooks) == 0:
    #         top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]
    # else:
    #     top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]


    # context["ebooks"] = top_3_ebooks
    # context["formations"] = formation_list
    context["events"] = page_obj
    context["event_category_list"] = event_category_list
    return render(request, "event/index.html", context)

def detail(request, event_id):
    target_event = EventModel.objects.get(id=event_id)
    # related_post_category = BlogPost.objects.filter(category=target_post.category.id).exclude(id=target_post.id)[:20]
    # formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
    #     video_count=Count('formationvideo__id'))[:2]
    
    # EbookModelWithSales = EbookModel.objects.annotate(
    #     sales_count=Count('saleebook__id')
    # )
    # top_3_ebooks = EbookModelWithSales.filter(category=target_post.category.id).order_by('-sales_count')[:3]
    # if len(top_3_ebooks) == 0:
    #     top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]

    context = {
        "event": target_event,
        # "ebooks": top_3_ebooks,
        # "formations": formation_list,
        # "related_post_category": related_post_category,
    }
    return render(request, "event/details.html", context)



from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import EbookModel, SaleEbook
from django.template import loader
from django.urls import reverse
from core.models import CategoryModel
from django.core.paginator import Paginator

def index(request: WSGIRequest):

    # category_id = request.GET.get("category_id")
    category_list = CategoryModel.objects.filter(ebookmodel__isnull=False)
    context = {}
    # if category_id is not None:
    #     ebook_list = EbookModel.objects.filter(category=category_id)
    #     target_category = [cat for cat in category_list if cat.id == int(category_id)]
    #     if len(target_category) != 0:
    #         context["category"] = target_category[0]
    # else:
    # ebook_list = 
        
    # paginator = Paginator(latest_ebook_list, 6)

    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number if page_number is not None else 1)
    context["ebooks"] = EbookModel.objects.all().order_by("category")
    context["post_category_list"] = category_list
    # context["categories"] = categories
    return render(request, "ebook/index.html", context)

def detail(request, ebook_id):
    target_ebook = EbookModel.objects.get(id=ebook_id)
    related_ebook_category = EbookModel.objects.filter(category=target_ebook.category.id).exclude(id=target_ebook.id)[:4]
    if len(related_ebook_category) == 0:
        related_ebook_category = EbookModel.objects.all().order_by("-created_at").exclude(id=target_ebook.id)[:4]

    context = {
        "ebook": target_ebook,
        "related_ebook_category": related_ebook_category,
    }
    
    return render(request, "ebook/detail.html", context)


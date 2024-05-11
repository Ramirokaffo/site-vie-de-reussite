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
    # WSGIRequest.get_host
    category_list = CategoryModel.objects.filter(ebookmodel__isnull=False)
    context = {}

    context["ebooks"] = EbookModel.objects.all().order_by("category")
    context["post_category_list"] = category_list
    context["title"] = "Ebooks | Site vie de réussite"
    return render(request, "ebook/index.html", context)

def detail(request, ebook_id):
    target_ebook = EbookModel.objects.get(id=ebook_id)
    related_ebook_category = EbookModel.objects.filter(category=target_ebook.category.id).exclude(id=target_ebook.id)[:4]
    if len(related_ebook_category) == 0:
        related_ebook_category = EbookModel.objects.all().order_by("-created_at").exclude(id=target_ebook.id)[:4]

    context = {
        "ebook": target_ebook,
        "title": target_ebook.title,
        "related_ebook_category": related_ebook_category,
    }
    
    return render(request, "ebook/detail.html", context)


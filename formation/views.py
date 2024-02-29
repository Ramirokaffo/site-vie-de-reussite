from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Formation, SaleFormation
from django.template import loader
from django.urls import reverse
from core.models import CategoryModel
from django.core.paginator import Paginator
from django.db.models import Count


def index(request: WSGIRequest):
    category_list = CategoryModel.objects.filter(formation__isnull=False, formation__published=True)
    context = {}
    formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
        video_count=Count('formationvideo__id')
    )
    context["formations"] = formation_list
    context["formation_category_list"] = category_list
    return render(request, "formation/index.html", context)

def detail(request, formation_id):
    target_formation = Formation.objects.annotate(
        video_count=Count('formationvideo')
    )
    target_formation = target_formation.get(id=formation_id)
    related_formation_category = Formation.objects.filter(category=target_formation.category.id).exclude(id=target_formation.id)
    if len(related_formation_category) == 0:
        related_formation_category = Formation.objects.all().exclude(id=target_formation.id)[:4]
    context = {
        "formation": target_formation,
        "related_formation_category": related_formation_category,
    }
    return render(request, "formation/detail.html", context)


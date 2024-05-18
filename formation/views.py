from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Formation, SaleFormation, VideoComment, FormationVideo
from django.template import loader
from django.urls import reverse
from core.models import CategoryModel
from django.core.paginator import Paginator
from django.db.models import Count
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

def index(request: WSGIRequest):
    category_list = CategoryModel.objects.filter(formation__isnull=False, formation__published=True)
    context = {}
    formation_list = Formation.objects.filter(published=True).order_by("category").annotate(
        video_count=Count('formationvideo__id')
    )
    context["formations"] = formation_list
    context["formation_category_list"] = category_list
    context["title"] = "Formations | Site vie de réussite"
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
        "title": target_formation.title,
        "related_formation_category": related_formation_category,
    }
    return render(request, "formation/detail.html", context)


@csrf_exempt
def comment(request: WSGIRequest):
    data = request.body.decode()
    data = json.loads(data)
    videoComment = VideoComment(content=data["userComment"], author=User(id=data["userId"]), video=FormationVideo(data["videoId"]))
    videoComment.save()
    videoComment.author = request.user
    serialized_user = serialize('json', [request.user])
    return JsonResponse({"status": "1", "comment": {"content": videoComment.content}, "author": serialized_user}, content_type='application/json')


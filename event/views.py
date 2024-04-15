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

    context["events"] = page_obj
    context["title"] = "Évènements | Site vie de réussite"
    context["event_category_list"] = event_category_list
    return render(request, "event/index.html", context)

def detail(request, event_id):
    target_event = EventModel.objects.get(id=event_id)

    context = {
        "event": target_event,
        "title": target_event.title,
    }
    return render(request, "event/details.html", context)



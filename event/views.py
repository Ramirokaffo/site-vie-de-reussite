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
from datetime import datetime
from django.utils import timezone


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
    context["selected_tab"] = "event"
    context["title"] = "Évènements | Site vie de réussite"
    context["event_category_list"] = event_category_list
    return render(request, "event/index.html", context)

def detail(request, event_id):
    target_event = EventModel.objects.get(id=event_id)
    startDate = datetime.strptime(str(target_event.start_at)[:-6], "%Y-%m-%d %H:%M:%S")
    endDate = datetime.strptime(str(target_event.end_at)[:-6], "%Y-%m-%d %H:%M:%S")

    startDate = timezone.make_aware(startDate, timezone.get_default_timezone())
    endDate = timezone.make_aware(endDate, timezone.get_default_timezone())
    now = timezone.now()
    show_inscription_link: bool = False
    if ((startDate < now and now < endDate) and target_event.inscription_link is not None ) or (startDate > now and target_event.inscription_link is not None) :
        show_inscription_link = True

    context = {
        "event": target_event,
        "selected_tab": "event",
        "title": target_event.title,
        "show_inscription_link": show_inscription_link,
    }
    return render(request, "event/details.html", context)



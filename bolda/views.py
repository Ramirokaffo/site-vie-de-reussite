from django.shortcuts import render
from blog.models import BlogPost
from ebook.models import EbookModel
from testimony.models import TestimonyModel
from formation.models import Formation
from event.models import EventModel
from django.db.models import Count
from core.models import SiteVideoModel
from django.contrib.auth import login
from django.core.handlers.wsgi import WSGIRequest
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from bolda.settings import MEDIA_ROOT
from .py_script import get_images_url as get_images_url_func
from .py_script import delete_migrations_files as delete_migrations_files_func

def index(request: WSGIRequest):
    latest_post_list = BlogPost.objects.filter(published=True)[:3]
    # latest_post_list[0].author.get_full_name
    # Annoter le modèle EbookModel avec le nombre de ventes
    EbookModelWithSales = EbookModel.objects.annotate(
        sales_count=Count('saleebook__id')
    )
 
    # Obtenir les 3 ebooks avec les plus grandes ventes
    top_3_ebooks = EbookModelWithSales.filter(published=True).order_by('-sales_count')[:3]

    # Annoter le modèle EbookModel avec le nombre de ventes
    FormationModelWithSales = Formation.objects.annotate(
        sales_count=Count('saleformation__id')
    )

    # Obtenir les 3 ebooks avec les plus grandes ventes
    top_2_formations = FormationModelWithSales.filter(published=True).order_by('-sales_count')[:2]

    last_testimony_list = TestimonyModel.objects.filter(is_visible=True).select_related("author__userprofilmodel").order_by("-created_at")[:10]
    event_list = EventModel.objects.filter(published=True)[:8]

    site_videos = SiteVideoModel.objects.filter(published=True, show_where="home")[:6]

    context = {
        "last_testimony_list": last_testimony_list,
        "ebooks": top_3_ebooks,
        "events": event_list,
        "formations": top_2_formations,
        "posts": latest_post_list,
        "site_videos": site_videos,
        "selected_tab": "home",
        "title": "Coaching et développement personnel avec Dr. Tara Bolda | Vie de réussite",
    }
    last_navigation = request.session.get("last_navigation")

    if (last_navigation is None) or (datetime.fromisoformat(last_navigation) + timedelta(days=1) < datetime.now()):
        request.session["last_navigation"] = datetime.now().isoformat()
        event_to_show = EventModel.objects.filter(show_at_home=True)[:1]
        context["event_to_show"] = event_to_show[0] if len(event_to_show) != 0 else None
    

    return render(request=request, template_name="index.html", context=context)



def about(request):
    context = {
        "selected_tab": "about",
        "title": "À propos de nous"
    }
    return render(request, template_name="about.html", context=context)
    # return render(request, template_name="appointment/add_success.html", context=context)
    # return render(request=request, template_name="404.html", context=context)


    

def privacy(request):
    context = {
        "title": "Politique de confidentialité"
    }
    return render(request=request, template_name="privacy.html", context=context)


def legal_notice(request):
    context = {
        "title": "Mentions légales"
    }
    return render(request=request, template_name="legal_mention.html", context=context)


@csrf_exempt
def get_images_url(request: WSGIRequest):
    image_list = get_images_url_func(os.path.join(MEDIA_ROOT, "images"))
    return JsonResponse(image_list, content_type='application/json', safe=False)


# @csrf_exempt
# def delete_migrations_files(request: WSGIRequest):
#     delete_migrations_files_func()
#     return JsonResponse({"status": "ok"}, content_type='application/json', safe=False)


def web_hooks_end_point(request: WSGIRequest):
    print(request.GET)
    # reference = request.GET.get('reference')
    # trxref = request.GET.get('trxref')
    # notchpay_trxref = request.GET.get('notchpay_trxref')
    # status = request.GET.get('status')
    return JsonResponse({"status": "receive"})



from django.shortcuts import render
from blog.models import BlogPost
from ebook.models import EbookModel
from testimony.models import TestimonyModel
from formation.models import Formation
from event.models import EventModel
from django.db.models import Count


def index(request):
    latest_post_list = BlogPost.objects.all()[:3]

    # Annoter le modèle EbookModel avec le nombre de ventes
    EbookModelWithSales = EbookModel.objects.annotate(
        sales_count=Count('saleebook__id')
    )

    # Obtenir les 3 ebooks avec les plus grandes ventes
    top_3_ebooks = EbookModelWithSales.order_by('-sales_count')[:3]

    # Annoter le modèle EbookModel avec le nombre de ventes
    FormationModelWithSales = Formation.objects.annotate(
        sales_count=Count('saleformation__id')
    )

    # Obtenir les 3 ebooks avec les plus grandes ventes
    top_2_formations = FormationModelWithSales.order_by('-sales_count')[:2]

    last_testimony_list = TestimonyModel.objects.filter(is_visible=True)[:10]
    event_list = EventModel.objects.filter(published=True)[:8]
    context = {
        "last_testimony_list": last_testimony_list,
        "ebooks": top_3_ebooks,
        "events": event_list,
        "formations": top_2_formations,
        "posts": latest_post_list,
    }
    return render(request=request, template_name="index.html", context=context)
from django.shortcuts import render, redirect

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
from uuid import uuid4
from django.urls import reverse
from bolda.settings import NOTCH_PAY_PUBLIC_API_KEY
from requests import post
from django.contrib import messages


def index(request: WSGIRequest):
    category_list = CategoryModel.objects.filter(formation__isnull=False, formation__published=True)
    context = {}
    formation_list = Formation.objects.filter(published=True).order_by("category")
    # .annotate(
    #     video_count=Count('formationvideo__id')
    # )
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


def buy(request: WSGIRequest, formation_id: int):
    if request.user.is_authenticated:
        target_formation = Formation.objects.get(id=formation_id)
        url = "https://api.notchpay.co/payments/initialize"
        reference = uuid4()

        callback = request.build_absolute_uri(reverse('formation:formation_buy_callback'))
        data = {
            "email": request.user.email,
            "amount": target_formation.promo_price,
            "currency": "XAF",
            "description": f"Paiement de la formation {target_formation.title} | Site vie de réussite",  # Optional
            "reference": reference,
            "callback": callback
            # "callback": "https://webhook.site/fec75097-ec63-48bc-8e52-e17f51ea2316"
        }

        headers = {
            "Authorization": NOTCH_PAY_PUBLIC_API_KEY,
            "Cache-Control": "no-cache"
        }

        # Send POST request with data and headers
        response = post(url, data=data, headers=headers)

        # Check for successful response (usually status code 200)
        # print(response.json())
        if response.status_code == 201:
            payment_data = response.json()
            my_sale_ebook = SaleFormation.objects.create(user=request.user, formation=target_formation, amount=target_formation.promo_price, my_reference=reference, notch_pay_reference=payment_data["transaction"]["reference"])
            my_sale_ebook.save()

            return redirect(payment_data["authorization_url"])
        else:
            messages.error(request, "Une erreur s'est produite lors de l'initialisation de votre achat")
            return redirect(f'/formation/{formation_id}')
    else:
        return redirect(f"/auth/register?next={ '/formation/buy/' + str(formation_id) }")

def formation_buy_callback(request: WSGIRequest):
    reference = request.GET.get('reference')
    # trxref = request.GET.get('trxref')
    notchpay_trxref = request.GET.get('notchpay_trxref')
    status = request.GET.get('status')
    my_sale_formation = SaleFormation.objects.get(my_reference=notchpay_trxref, notch_pay_reference=reference)
    my_sale_formation.status = status
    if status == "complete":
        my_sale_formation.isPaid = True
    my_sale_formation.save()
    if status == "complete":
        return redirect("/profil/formation")
    else:
        messages.error(request, "Le paiement a échoué")
        return redirect(f"/formation/{my_sale_formation.formation.id}")

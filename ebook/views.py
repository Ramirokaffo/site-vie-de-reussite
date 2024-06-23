from django.shortcuts import render, redirect

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import EbookModel, SaleEbook
from django.template import loader
from django.urls import reverse
from core.models import CategoryModel
from django.core.paginator import Paginator
from requests import post
from bolda.settings import NOTCH_PAY_PUBLIC_API_KEY
from django.contrib import messages
from uuid import uuid4
from django.urls import reverse

def index(request: WSGIRequest):
    category_list = CategoryModel.objects.filter(ebookmodel__isnull=False)
    context = {}

    context["ebooks"] = EbookModel.objects.filter(published=True).order_by("category")
    context["post_category_list"] = category_list
    context["title"] = "Ebooks | Site vie de réussite"
    return render(request, "ebook/index.html", context)

def detail(request, ebook_id):
    target_ebook = EbookModel.objects.get(id=ebook_id)
    related_ebook_category = EbookModel.objects.filter(category=target_ebook.category.id, published=True).exclude(id=target_ebook.id)[:4]
    if len(related_ebook_category) == 0:
        related_ebook_category = EbookModel.objects.filter(published=True).order_by("-created_at").exclude(id=target_ebook.id)[:4]

    context = {
        "ebook": target_ebook,
        "title": target_ebook.title,
        "related_ebook_category": related_ebook_category,
    }
    
    return render(request, "ebook/detail.html", context)


def buy(request: WSGIRequest, ebook_id: int):
    if request.user.is_authenticated:
        target_ebook = EbookModel.objects.get(id=ebook_id)
        url = "https://api.notchpay.co/payments/initialize"
        reference = uuid4()

        callback = request.build_absolute_uri(reverse('ebook:ebook_buy_callback'))
        data = {
            "email": request.user.email,
            "amount": target_ebook.promo_price,
            "currency": "XAF",
            "description": f"Paiement de l'ouvrage {target_ebook.title} | Site vie de réussite",  # Optional
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
            my_sale_ebook = SaleEbook.objects.create(user=request.user, ebook=target_ebook, amount=target_ebook.promo_price, my_reference=reference, notch_pay_reference=payment_data["transaction"]["reference"])
            my_sale_ebook.save()

            return redirect(payment_data["authorization_url"])
        else:
            messages.error(request, "Une erreur s'est produite lors de l'initialisation de votre achat")
            return redirect(f'/ebook/{ebook_id}')
    else:
        return redirect("/auth/register")

def ebook_buy_callback(request: WSGIRequest):
    reference = request.GET.get('reference')
    # trxref = request.GET.get('trxref')
    notchpay_trxref = request.GET.get('notchpay_trxref')
    status = request.GET.get('status')
    my_sale_ebook = SaleEbook.objects.get(my_reference=notchpay_trxref, notch_pay_reference=reference)
    my_sale_ebook.status = status
    if status == "complete":
        my_sale_ebook.isPaid = True
    my_sale_ebook.save()
    if status == "complete":
        return redirect("/profil/ebook")
    else:
        messages.error(request, "Le paiement a échoué")
        return redirect(f"/ebook/{my_sale_ebook.ebook.id}")

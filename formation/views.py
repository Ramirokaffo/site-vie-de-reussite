from django.shortcuts import render, redirect

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Formation, SaleFormation, VideoComment, FormationVideo, PhysicFormationCmd
from django.urls import reverse
from core.models import CategoryModel
from django.db.models import Count
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from uuid import uuid4
from django.urls import reverse
from bolda.settings import NOTCH_PAY_PUBLIC_API_KEY
from requests import post
from django.contrib import messages

from bolda.settings import EMAIL_HOST_USER, MANAGERS
from django.core.mail import send_mail
from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import Http404


def index(request: WSGIRequest):
    # sendActivationEmail(request, request.user, "Mail de debogage", None)

    category_list = CategoryModel.objects.filter(formation__isnull=False, formation__published=True)
    context = {}
    formation_list = Formation.objects.filter(published=True).order_by("category")
    context["formations"] = formation_list
    context["selected_tab"] = "formation"
    context["formation_category_list"] = category_list
    context["title"] = "Formations | Site vie de réussite"
    return render(request, "formation/index.html", context)

def detail(request, formation_id):
    target_formation = Formation.objects.annotate(
        video_count=Count('formationvideo')
    )
    target_formation = target_formation.get(id=formation_id)
    if target_formation:
        target_formation = target_formation[0]
    else:
        raise Http404("Formation non trouvée")
    related_formation_category = Formation.objects.filter(category=target_formation.category.id).exclude(id=target_formation.id)
    if len(related_formation_category) == 0:
        related_formation_category = Formation.objects.all().exclude(id=target_formation.id)[:4]
    context = {
        "formation": target_formation,
        "selected_tab": "formation",
        "title": target_formation.title,
        "related_formation_category": related_formation_category,
    }
    return render(request, "formation/detail.html", context)


@csrf_exempt
@login_required
def comment(request: WSGIRequest):
    data = request.body.decode()
    data = json.loads(data)
    videoComment = VideoComment(content=data["userComment"], author=User(id=data["userId"]), video=FormationVideo(data["videoId"]))
    videoComment.save()
    videoComment.author = request.user
    serialized_user = serialize('json', [request.user])
    return JsonResponse({"status": "1", "comment": {"content": videoComment.content}, "author": serialized_user}, content_type='application/json')

def physic_command(request: WSGIRequest, formation_id: int):
    if request.POST:
        formations = Formation.objects.filter(id=formation_id)
        phone_number = request.POST.get("phone_number")
        if formations:
            formation = formations[0]
            cmd = PhysicFormationCmd.objects.create(formation=formation, 
                                                    phone_number=phone_number,
                                                    amount=formation.promo_price)
            cmd.save()
            notifiedManager(request, cmd)
    messages.success(request, "Votre commande a été enregistrée avec succès. Nous vous contacterons dans un plus brief délai")
    return redirect(f"/formation/{formation_id}")



def buy(request: WSGIRequest, formation_id: int):
    """
    Fonction qui initialise la transaction et redirige l'utilisateur vers la page de paiement
    """
    if request.user.is_authenticated:
        try:
            # Rechercher dans la base de données la formation que l'utilisateur veut acheter
            target_formation = Formation.objects.get(id=formation_id) # Si la formation n'existe pas, cette fonction va lever une exception
            url = "https://api.notchpay.co/payments/initialize"
            # Generer une reference unique et aleatoire pour suivre la transaction
            reference = uuid4()
            # Generer le lien de redirection à utiliser une transaction terminée
            callback = request.build_absolute_uri(reverse('formation:formation_buy_callback'))
            data = {
                "email": request.user.email,
                "amount": target_formation.promo_price,
                "currency": "XAF",
                "description": f"Paiement de la formation {target_formation.title} | Site vie de réussite",  # Optional
                "reference": reference,
                "callback": callback
            }

            headers = {
                "Authorization": NOTCH_PAY_PUBLIC_API_KEY,
                "Cache-Control": "no-cache"
            }

            # Envoyer les données de la transaction à l'API de Notch Pay
            response = post(url, data=data, headers=headers)

            # Vérifier si tous s'est bien passé
            if response.status_code == 201:
                payment_data = response.json()
                # Enregistrer l'achat au préalable mais avec un statut NON PAYÉ
                my_sale_ebook = SaleFormation.objects.create(user=request.user, formation=target_formation, amount=target_formation.promo_price, my_reference=reference, notch_pay_reference=payment_data["transaction"]["reference"])
                my_sale_ebook.save()
                # Rediriger l'utilisateur vers la page de paiement retourné par Notch Pay
                return redirect(payment_data["authorization_url"])
            else:
                messages.error(request, "Une erreur s'est produite lors de l'initialisation de votre achat")
                return redirect(f'/formation/{formation_id}')
        except:
            messages.error(request, "Une erreur s'est produite lors de l'initialisation de votre achat")
            return redirect(f'/formation/{formation_id}')
    else:
        return redirect(f"/auth/register?next={ '/formation/buy/' + str(formation_id) }")

def formation_buy_callback(request: WSGIRequest):
    """
    Fonction qui est appélée lorsque l'utilisateur termine ou annule sa transaction
    """
    # Recuperer la reference de Notch Pay
    reference = request.GET.get('reference')
    # Recuperer la reference de la transaction provenant de mon site [reference = uuid4()]
    notchpay_trxref = request.GET.get('notchpay_trxref')
    # Recuperer le status de la transaction provenant de Notch Pay
    status = request.GET.get('status')
    my_sale_formation = SaleFormation.objects.get(my_reference=notchpay_trxref, notch_pay_reference=reference)
    my_sale_formation.status = status
    # Si le statut de la transaction est [complete], cela veut dire que l'utilisateur a payé sa formation
    if status == "complete":
        my_sale_formation.isPaid = True
    my_sale_formation.save()
    if status == "complete":
        # Rediriger l'utilisateur sur son profil (Page des formations achetées)
        return redirect("/profil/formation")
    else:
        messages.error(request, "Le paiement a échoué")
        return redirect(f"/formation/{my_sale_formation.formation.id}")


def notifiedManager(request, cmd: PhysicFormationCmd):
    for manager in MANAGERS:
        confirm_maessage = render_to_string("formation/cmd_snippet.html", {
            "cmd": cmd,
            "rsrc_title": cmd.formation.title,
            "request": request,
            "manager": manager[0]
        })
    
        plain_message = strip_tags(confirm_maessage)
        send_mail(
        subject=f"Nouvelle commande ~ {cmd.phone_number}",
        message=plain_message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[manager[1]],
        html_message=confirm_maessage,
        fail_silently=True
    )

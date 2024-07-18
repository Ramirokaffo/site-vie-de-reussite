from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
import json
from django.http import JsonResponse
from .models import Subscribers
from django.shortcuts import render, redirect
from django.contrib import messages


@csrf_exempt
def subscribe(request: WSGIRequest):
    data = request.body.decode()
    data = json.loads(data)
    expected_subscriber = Subscribers.objects.filter(email=data["email"])
    if not expected_subscriber:
        subscriber = Subscribers(email=data["email"])
        subscriber.save()
        return JsonResponse({"status": "1"}, content_type='application/json')
    return JsonResponse({"status": "0"}, content_type='application/json')



def unsubscribe(request: WSGIRequest):
    if request.POST:
        email = request.POST.get("email")
        expected_subscriber = Subscribers.objects.filter(email=email)
        if expected_subscriber:
            expected_subscriber[0].is_subscrib = False
            expected_subscriber[0].save()
            return render(request, "newsletter/unsubscribe_success.html")
        else:
            messages.error(request=request, message="La desinscription a échouée !")
            redirect("/newsletter/unsubscribe")
    return render(request, "newsletter/unsubscribe.html")
    # return render(request, "newsletter/unsubscribe_success.html")




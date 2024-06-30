from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
import json
from django.http import JsonResponse
from .models import Subscribers

@csrf_exempt
def subscribe(request: WSGIRequest):
    data = request.body.decode()
    data = json.loads(data)
    subscriber = Subscribers(email=data["email"])
    subscriber.save()
    return JsonResponse({"status": "1"}, content_type='application/json')

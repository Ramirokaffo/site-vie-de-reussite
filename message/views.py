from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from message.models import Message
import json
from django.http import JsonResponse

def add(request: WSGIRequest):
    data = request.body.decode()
    data = json.loads(data)
    message = Message(name=data["name"], email=data["email"], content=data["message"])
    message.save()
    return JsonResponse({"status": "1"})

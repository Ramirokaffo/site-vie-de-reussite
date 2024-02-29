from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from appointment.models import AppointmentModel
import json
from django.http import JsonResponse

def add(request: WSGIRequest):
    full_name = request.POST.get("full_name")
    phone_number = request.POST.get("phone_number")
    my_date = request.POST.get("my_date")
    gender = request.POST.get("gender")
    objectif = request.POST.get("objectif")
    country = request.POST.get("country")
    city = request.POST.get("city")
    email = request.POST.get("email")
    
    appointment = AppointmentModel(full_name=full_name, 
                               gender=gender, 
                               phone_number=phone_number, 
                               country=country, 
                               city=city, 
                               email=email, 
                               my_date=my_date, 
                               objectif=objectif)
    appointment.save()
    return render(request, "appointment/add_success.html")

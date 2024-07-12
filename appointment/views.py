from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from appointment.models import AppointmentModel


from bolda.settings import EMAIL_HOST_USER, MANAGERS
from django.core.mail import send_mail
from django.utils.http import  urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags


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
    notifiedManager(request, appointment)
    return render(request, "appointment/add_success.html")


def notifiedManager(request, appointment: AppointmentModel):
    print(MANAGERS)
    for manager in MANAGERS:
        confirm_maessage = render_to_string("appointment/appointment_snippet.html", {
            "appointment": appointment,
            "request": request,
            "manager": manager[0]
        })
    
        plain_message = strip_tags(confirm_maessage)
        send_mail(
        subject=f"Nouveau rendez-vous ~ {appointment.full_name}",
        message=plain_message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[manager[1]],
        html_message=confirm_maessage,
        fail_silently=True
    )

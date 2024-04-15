from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from bolda import settings
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .token import generatorToken

def index(request):
        if request.POST:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active == False:
                    messages.error(request, "Vous n'avez pas encore activé votre compte; veuillez verifier votre adresse email")
                    return redirect("login")
                login(request, user)
                messages.success(request, "Authentification reussie")
                return redirect("/profil", request=request, context={"user": user})
            else:
                messages.error(request, "L'authentification a échoué")
                return redirect("/auth/login")
        else:
            if request.user.is_authenticated:
                return redirect("/profil", request=request)
            return render(request, "auth/login.html", context={"title": "Connexion"})



def register(request):

    if request.POST:
        # username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        email = request.POST.get("email")

        if User.objects.filter(username=email):
            messages.error(request, "Cette adresse mail est deja utilisée")
            return redirect("/auth/register")
        if password != password1:
            messages.error(request, "Mot de passe non correspondant !")
            return redirect("register")

        print(firstname, lastname, password, password1, email)
        myUser = User.objects.create_user(email=email, username=email, password=password, last_name=lastname, first_name=firstname)
        # myUser.is_active = False
        myUser.save()
        messages.success(request, "Votre compte a été créé avec succès !")
    #     subject = "Bienvenue sur notre application"
    #     message = f"Bienvenue {myUser.first_name} {myUser.last_name} \n Nous sommes heureux de vous compter parmi nous \n\n\n Merci ! \n\n Ramiro Kaffo"
    #     from_email = settings.EMAIL_HOST_USER
    #     to_list = [myUser.email]
    #     send_mail(subject, message, from_email, to_list, fail_silently=False)
        
    #     current_site = get_current_site(request)
    #     confirm_subject = "Confirmation de l'adresse email"
    #     confirm_maessage = render_to_string("email_confirm.html", {
    #         "name": myUser.first_name,
    #         "domain":current_site.domain,
    #         "uid": urlsafe_base64_encode(force_bytes(myUser.pk)),
    #         "token": generatorToken.make_token(myUser),
    #     })
    #     email = EmailMessage(
    #         confirm_subject,
    #         confirm_maessage,
    #         settings.EMAIL_HOST_USER,
    #         [myUser.email]
    #     )

    #     email.fail_silently = False
    #     email.send()
        
        return redirect("/auth/login")
    
    return render(request, "auth/register.html", context={"title": "Création de compte"})


def log_out(request: WSGIRequest):
    logout(request)
    return redirect("/auth/login")
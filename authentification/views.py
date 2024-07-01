from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from bolda.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.handlers.wsgi import WSGIRequest
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .token import generatorToken
from django.utils.html import strip_tags


def index(request: WSGIRequest):
        next = request.GET.get("next")    
        if request.POST:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(username=email, password=password)            
            if user is None:
                expectedUser = User.objects.filter(email=email)
                if expectedUser:
                    user = authenticate(username=expectedUser[0].username, password=password)
            if user is not None:
                if user.is_active == False:
                    messages.error(request, "Vous n'avez pas encore activé votre compte; veuillez verifier votre adresse email")
                    return redirect(f"/auth/login?next={next}" if next is not None else "/auth/login")
                login(request, user)
                messages.success(request, "Authentification réussie")
                if next is not None:
                    return redirect(next)
                return redirect("/profil", request=request, context={"user": user})
            else:
                expected_user = User.objects.filter(email=email)
                if expected_user:
                    if not expected_user[0].is_active:
                        messages.error(request, "Votre compte n'est pas activé. Nous vous avons envoyé un mail d'activation")
                    else:
                        messages.error(request, "L'authentification a échoué")
                else:
                    messages.error(request, "L'authentification a échoué")
                return redirect(f"/auth/login?next={next}" if next is not None else "/auth/login")
        else:
            if request.user.is_authenticated:
                return redirect("/profil", request=request)
            # return render(request, "auth/reset_password.html", context={"title": "Connexion"})
            return render(request, "auth/login.html", context={"title": "Connexion", "next": next})



def register(request):
    next = request.GET.get("next")    

    if request.POST:
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        email = request.POST.get("email")

        if User.objects.filter(username=email):
            messages.error(request, "Cette adresse mail est déjà utilisée")
            return redirect("/auth/register" if next is None else f"/auth/register?next={next}")
        
        if password != password1:
            messages.error(request, "Mot de passe non correspondant !")
            return redirect("/auth/register" if next is None else f"/auth/register?next={next}")

        myUser = User.objects.create_user(email=email, username=email, password=password, last_name=lastname, first_name=firstname)
        myUser.is_active = False
        myUser.save()
        messages.success(request, "Votre compte a été créé avec succès ! Nous vous avons envoyé un mail d'activation")

        confirm_subject = "Activation de votre compte sur le site Vie de réussite"
        sendActivationEmail(request=request, confirm_subject=confirm_subject, myUser=myUser, next=next)
        
        return redirect("/auth/login" if next is None else f"/auth/login?next={next}")
    
    return render(request, "auth/register.html", context={"title": "Création de compte", "next": next})



def reset(request):
    next = request.GET.get("next")    

    if request.POST:
        email = request.POST.get("email")
        myUser = User.objects.filter(email=email)
        if myUser:
            myUser = myUser[0]
            messages.info(request, "Un lien de réinitialisation a été envoyé sur votre adresse mail")
            confirm_subject = "Réinitialisation du mot de passe de votre compte sur le site Vie de réussite"
            sendResetEmail(request=request, confirm_subject=confirm_subject, myUser=myUser, next=next)
            return redirect("/auth/login" if next is None else f"/auth/login?next={next}")
        else:
            messages.error(request, "Compte introuvable !")
            return redirect("/auth/reset" if next is None else f"/auth/reset?next={next}")
    else:
        return render(request, "auth/reset_password.html", context={"title": "Mot de passe oublié", "next": next})



def activate(request: WSGIRequest, uidb64, token):
    next = request.GET.get("next")    
    if not request.POST:
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            myUser =  User.objects.get(id=int(uid))
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            myUser = None
        if myUser is not None and generatorToken.check_token(myUser, token):
            myUser.is_active = True
            myUser.save()
            messages.success(request, "Votre adresse e-mail a été confirmée avec succès ! Vous pouvez vous connecter maintenant")
            return redirect("/auth/login" if next is None else f"/auth/login?next={ next }")
        else:
            messages.error(request, "Le lien de confirmation n\'est pas valide ou a expiré.")
        return redirect("/auth/login" if next is None else f"/auth/login?next={ next }")
    else:
        email = request.POST.get("email")
        try:
            expexted_user = User.objects.get(email=email)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return redirect("/auth/login" if next is None else f"/auth/login?next={ next }")
        confirm_subject = "Confirmation de mot de passe"
        sendActivationEmail(request=request, confirm_subject=confirm_subject, myUser=expexted_user, next=next)
        return redirect("/auth/login" if next is None else f"/auth/login?next={ next }")


def new_password(request: WSGIRequest, uidb64):
    next = request.GET.get("next")    
    if not request.POST:
        return render(request, "auth/new_password.html", context={"title": "Nouveau mot de passe", "next": next, "uid": uidb64})
    else:
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        if password != password1:
            messages.error(request, "Mot de passe non correspondant !")
            return redirect(f"/auth/new_password/{uidb64}" if next is None else f"/auth/new_password/{uidb64}?next={ next }")
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=int(uid))
        user.set_password(password)
        user.save()
        print(user)
        print(user.check_password(password))
        messages.success(request, "Votre mot de passe a été rénitialisé avec succès; Vous pouvez vous connecter !")
        return redirect("/auth/login" if next is None else f"/auth/login?next={ next }")


def reset_pwd(request: WSGIRequest, uidb64, token):
    next = request.GET.get("next")   
    if not request.POST:
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            myUser =  User.objects.get(id=int(uid))
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            myUser = None
        if generatorToken.check_token(myUser, token):
            messages.success(request, "Renseignez votre nouveau mot de passe !")
            return redirect(f"/auth/new_password/{uidb64}" if next is None else f"/auth/new_password/{uidb64}?next={ next }")
        else:
            
            messages.error(request, "Le lien de réinitialisation n\'est pas valide ou a expiré.")        
        return redirect("/auth/reset" if next is None else f"/auth/reset?next={ next }")

    

def authMail(request: WSGIRequest):
    next = request.GET.get("next")    

    if not request.POST:
        return render(request, "auth/ask_email.html", context={"title": "Mail de recupération/activation", "next": next})
    else:
        username = request.POST.get("username")
        try:
            expected_user = User.objects.get(username=username)
            confirm_subject = "Changement de mot de passe"
            sendActivationEmail(request=request, confirm_subject=confirm_subject, myUser=expected_user, next=next)            
            messages.success(request, "Un mail d'activation a été envoyé sur votre adresse ! Veuillez vérifier votre boîte mail " + expected_user.username)
            return redirect("/auth/login" if next is None else f"/auth/login?next={next}")
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            messages.error(request, "Impossible d'envoyer le lien d'activation. Veuillez vérifier votre adresse mail/nom d'utilisateur !")
            return redirect("/auth/authMail" if next is None else f"/auth/authMail?next={ next }")
        
    


def log_out(request: WSGIRequest):
    logout(request)
    return redirect("/auth/login")


def sendActivationEmail(request, myUser, confirm_subject, next):
    current_site = get_current_site(request)

    confirm_maessage = render_to_string("auth/email_confirm.html", {
            "first_name": myUser.first_name,
            "last_name": myUser.last_name,
            "request": request,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(myUser.pk)),
            "token": generatorToken.make_token(myUser),
            "next": next

        })
    plain_message = strip_tags(confirm_maessage)
    return send_mail(
        subject=confirm_subject,
        message=plain_message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[myUser.email],
        html_message=confirm_maessage,
        fail_silently=True
    )


def sendResetEmail(request, myUser, confirm_subject, next):
    current_site = get_current_site(request)

    confirm_maessage = render_to_string("auth/password_reset_email.html", {
            "first_name": myUser.first_name,
            "last_name": myUser.last_name,
            "request": request,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(myUser.pk)),
            "token": generatorToken.make_token(myUser),
            "next": next

        })
    plain_message = strip_tags(confirm_maessage)
    return send_mail(
        subject=confirm_subject,
        message=plain_message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[myUser.email],
        html_message=confirm_maessage,
        fail_silently=True
    )

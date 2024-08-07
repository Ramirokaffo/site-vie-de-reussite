from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from profil.models import UserProfilModel  # Remplacez par le nom de votre modèle de profil
from django.core.handlers.wsgi import WSGIRequest

@receiver(user_logged_in)
def add_user_profile_to_session(sender, request: WSGIRequest, user, **kwargs):
    """
    Ajoute le profil utilisateur à la session lors de la connexion.
    """

    try:
        # Récupérer le profil associé à l'utilisateur
        expected_user_profile = UserProfilModel.objects.filter(user=user)
        print(expected_user_profile)
        if expected_user_profile:
            user_profile = expected_user_profile[0]
        else:
            user_profile = UserProfilModel.objects.create(user=user)
            user_profile.save()
        print(user_profile)
        # Ajouter le profil à la session
        request.session['user_profile'] = {
            'id': user_profile.id,
        }
        if user_profile.profil_image:
            request.session['user_profile'] = {
            "profil_image": user_profile.profil_image.url
        }
        request.session.save()
    except:
        pass


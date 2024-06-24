from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from profil.models import UserProfilModel  # Remplacez par le nom de votre modèle de profil

@receiver(user_logged_in)
def add_user_profile_to_session(sender, request, user, **kwargs):
    """
    Ajoute le profil utilisateur à la session lors de la connexion.
    """

    try:
        # Récupérer le profil associé à l'utilisateur
        user_profile = UserProfilModel.objects.get(user=user)

        # Ajouter le profil à la session
        request.session['user_profile'] = {
            'id': user_profile.id,
            "profil_image": user_profile.profil_image.url
        }
    except:
        pass


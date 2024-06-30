from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from newsletter.models import Subscribers


class MyAdminSite(admin.AdminSite):
    site_header = "Administration du site vie de réussite"
    


class MyUserAdmin(UserAdmin):

    actions = ['supprimer_utilisateurs_selectionnes', 
               'desactiver_utilisateurs_selectionnes', 
               'activer_utilisateurs_selectionnes',
               'ajouter_a_liste_diffusion']
    save_on_top = True

    def ajouter_a_liste_diffusion(self, request, queryset):
        for user in queryset:
            expected_subscriber = Subscribers.objects.filter(email=user.email)
            if not expected_subscriber:
                Subscribers.objects.create(email=user.email, first_name=user.first_name, last_name=user.last_name).save()
        self.message_user(request, _("Les utilisateurs sélectionnés ont été ajoutés à la liste de diffusion."))

    def desactiver_utilisateurs_selectionnes(self, request, queryset):
        """Désactive les utilisateurs sélectionnés."""
        queryset.update(is_active=False)
        self.message_user(request, _("Les utilisateurs sélectionnés ont été désactivés."))

    def activer_utilisateurs_selectionnes(self, request, queryset):
        """Active les utilisateurs sélectionnés."""
        queryset.update(is_active=True)
        self.message_user(request, _("Les utilisateurs sélectionnés ont été activés."))

    ajouter_a_liste_diffusion.short_description = _("Ajouter les utilisateurs sélectionnés à la liste de diffusion")
    desactiver_utilisateurs_selectionnes.short_description = _("Désactiver les utilisateurs sélectionnés")
    activer_utilisateurs_selectionnes.short_description = _("Activer les utilisateurs sélectionnés")



admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

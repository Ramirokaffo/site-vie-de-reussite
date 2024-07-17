from django.contrib import admin

from .models import AppointmentModel
from newsletter.models import Subscribers
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class AppointmentAdmin(admin.ModelAdmin):


    list_display = ("full_name", "country", "city", "my_date", "phone_number", "email", "objectif", "gender")
    date_hierarchy = "my_date"
    list_filter = ["country", "city", "gender"]
    search_fields = ["fullname", "objectif"]
    search_help_text = "Rechercher dans les rendez-vous"
    actions = ["subscribe_to_newsletter"]



    @admin.action(description="Ajouter les utilisateurs sélectionnés à la liste de diffusion")
    def subscribe_to_newsletter(self, request, queryset):
        appointment: AppointmentModel
        for appointment in queryset:
            expected_subscriber = Subscribers.objects.filter(email=appointment.email)
            if not expected_subscriber:
                Subscribers.objects.create(email=appointment.email, first_name=appointment.full_name).save()
        self.message_user(request, _("Les utilisateurs sélectionnés ont été ajoutés à la liste de diffusion."))



admin.site.register(AppointmentModel, AppointmentAdmin)

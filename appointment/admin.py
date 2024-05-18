from django.contrib import admin

from .models import AppointmentModel
from django.utils.html import format_html


class AppointmentAdmin(admin.ModelAdmin):


    list_display = ("full_name", "country", "city", "my_date", "phone_number", "email", "objectif", "gender")
    date_hierarchy = "my_date"
    list_filter = ["country", "city", "gender"]
    search_fields = ["fullname", "objectif"]
    search_help_text = "Rechercher dans les rendez-vous"


admin.site.register(AppointmentModel, AppointmentAdmin)

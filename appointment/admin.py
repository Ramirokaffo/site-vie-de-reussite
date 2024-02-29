from django.contrib import admin

from .models import AppointmentModel
from django.utils.html import format_html


class AppointmentAdmin(admin.ModelAdmin):


    list_display = ("full_name", "country", "city", "my_date", "phone_number", "email", "objectif", "gender")
    # list_editable = ("my_date", )


admin.site.register(AppointmentModel, AppointmentAdmin)

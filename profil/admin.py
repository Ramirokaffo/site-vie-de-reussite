from django.contrib import admin

from .models import UserProfilModel

class UserProfilAdmin(admin.ModelAdmin):

    list_display = ("user", "created_at")
    date_hierarchy = "created_at"
    # list_filter = ["country", "city", "gender"]
    search_fields = ["user__first_name", "user__last_name", "user__username"]
    search_help_text = "Rechercher dans les profils d'utilisateur"

admin.site.register(UserProfilModel, UserProfilAdmin)
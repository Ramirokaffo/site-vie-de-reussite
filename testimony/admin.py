from django.contrib import admin

from .models import TestimonyModel

class TestimonyAdmin(admin.ModelAdmin):
    list_display = (str, "is_visible")
    date_hierarchy = "created_at"
    list_filter = ["author", "is_visible"]



admin.site.register(TestimonyModel, TestimonyAdmin)

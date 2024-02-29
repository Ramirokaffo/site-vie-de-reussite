from django.contrib import admin

from .models import TestimonyModel

class TestimonyAdmin(admin.ModelAdmin):
    list_display = (str, "is_visible")


admin.site.register(TestimonyModel, TestimonyAdmin)

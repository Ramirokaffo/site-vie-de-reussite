from django.contrib import admin

from .models import FaqModel
from django.utils.html import format_html


class EbookAdmin(admin.ModelAdmin):

    list_display = ("name", "published", "normal_price", "promo_price", "created_at", "illustration_img", "illustration_vdeo")
    list_editable = ("published", )


admin.site.register(FaqModel)

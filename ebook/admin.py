from django.contrib import admin

from .models import EbookModel, SaleEbook
from django.utils.html import format_html


class EbookAdmin(admin.ModelAdmin):

    def illustration_img(self, obj):
        try:
            obj.illustration_image.url
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.illustration_image.url))
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")
    
    def illustration_vdeo(self, obj):
        try:
            # obj.illustration_video
            # return format_html(f'<video style="width:100px; height:100px;" controls> \
            #                    <source src="{obj.illustration_video}" type="video/mp4"> \
            #                    <source src="{obj.illustration_video}" type="video/mov"> \
            #                    <source src="{obj.illustration_video}" type="video/avi"> \
            #                     Your browser does not support the video tag.</video>')
             return format_html(f'''<iframe width="100px" height="100px" src="{obj.illustration_video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "published", "normal_price", "promo_price", "created_at", "illustration_img", "illustration_vdeo")
    list_editable = ("published", )


admin.site.register(EbookModel, EbookAdmin)
admin.site.register(SaleEbook)
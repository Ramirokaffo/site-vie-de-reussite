from django.contrib import admin
from django.utils.html import format_html

from .models import Formation, FormationVideo, VideoComment, SaleFormation


class FormationAdmin(admin.ModelAdmin):

    def illustration_img(self, obj):
        try:
            obj.illustration_image.url
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.illustration_image.url))
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")
    
    def illustration_vdeo(self, obj):
        try:
            return format_html(f'''<iframe width="100px" height="100px" src="https://www.youtube.com/embed/{obj.illustration_video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')

        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "category", "published", "normal_price", "promo_price", "created_at", "illustration_img", "illustration_vdeo")
    list_editable = ("published", )


class FormationVideoAdmin(admin.ModelAdmin):


    def illustration_img(self, obj):
        try:
            obj.illustration_image.url
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.illustration_image.url))
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")
    
    def vdeo(self, obj):
        try:
            return format_html(f'''<iframe width="100px" height="100px" src="https://www.youtube.com/embed/{obj.video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "formation", "published", "created_at", "vdeo")
    list_editable = ("published", )


class VideoCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "published", "created_at", "video", "author")
    list_editable = ("published", )


class SaleFormationAdmin(admin.ModelAdmin):
    list_display = ("formation", "user", "isPaid", "amount", "created_at")
    # list_editable = ("published", )



admin.site.register(Formation, FormationAdmin)
admin.site.register(SaleFormation, SaleFormationAdmin)
admin.site.register(FormationVideo, FormationVideoAdmin)
admin.site.register(VideoComment, VideoCommentAdmin)

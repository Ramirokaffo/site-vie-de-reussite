from django.contrib import admin
from django.utils.html import format_html

from .models import CategoryModel, SiteVideoModel

class SiteVideoAdmin(admin.ModelAdmin):

    def vdeo(self, obj):
        try:
            return format_html(f'''<iframe width="100px" height="100px" src="https://www.youtube.com/embed/{obj.video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "show_where", "published", "created_at", "vdeo")
    list_editable = ("published", )


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
     


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(SiteVideoModel, SiteVideoAdmin)


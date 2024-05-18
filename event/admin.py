from django.contrib import admin

from .models import EventModel
from django.utils.html import format_html


class EventAdmin(admin.ModelAdmin):

    def illustration_img(self, obj):
        try:
            obj.illustration_image.url
            return format_html('<a href="{}" style="display: inline;"><img src="{}" style="max-width:100px; max-height:100px; background-position:center; background-size:cover;"/></a>'.format(obj.illustration_image.url, obj.illustration_image.url))
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")
    
    def illustration_vdeo(self, obj):
        try:
             return format_html(f'''<iframe width="100px" height="100px" src="https://www.youtube.com/embed/{obj.illustration_video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "published", "start_at", "end_at", "created_at", "illustration_img", "illustration_vdeo", "show_at_home")
    list_editable = ("published", "show_at_home")
    list_filter = ["category", "published"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["category"]

    search_fields = ["title", "subtitle", "category__name"]
    search_help_text = "Rechercher un évènement via son titre, sous-titre ou sa catégorie"
    # raw_id_fields = ["category"]
    save_as = True
    save_on_top = True

    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les évènements selectionnés")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les évènements selectionnés")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)





admin.site.register(EventModel, EventAdmin)

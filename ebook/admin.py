from django.contrib import admin

from .models import EbookModel, SaleEbook, PhysicEbookCmd
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
             return format_html(f'''<iframe width="100px" height="100px" src="https://www.youtube.com/embed/{obj.illustration_video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "published", "normal_price", "promo_price", "created_at", "illustration_img", "illustration_vdeo")
    list_editable = ("published", )
    list_filter = ["category", "availability", "published"]
    search_fields = ["title", "subtitle", "category__name"]
    search_help_text = "Rechercher un ouvrage via son titre, sous-titre ou sa catégorie"

    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les ouvrages selectionnés")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les ouvrages selectionnés")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)



class SaleEbookAdmin(admin.ModelAdmin):


    list_display = ("ebook", "user", "amount", "isPaid", "status", "my_reference", "created_at", "last_updated")
    # list_editable = ("published", )
    list_filter = ["ebook", "isPaid", "status", "user"]
    search_fields = ["ebook__title", "user__username"]
    search_help_text = "Rechercher un ouvrage vendu via son titre ou le nom du client"

    # actions = ["make_published", "make_no_published"]

    # @admin.action(description="Définir les ouvrages selectionnés")
    # def make_published(self, request, queryset):
    #     queryset.update(isPaid=True)



    # @admin.action(description="Ne pas publier les ouvrages selectionnés")
    # def make_no_published(self, request, queryset):
    #     queryset.update(published=False)


class PhysicEbookCmdAdmin(admin.ModelAdmin):
    list_display = ("ebook", "phone_number", "isPaid", "amount", "created_at")

    list_filter = ["isPaid", "ebook"]
    search_fields = ["phone_number", "ebook__title"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["ebook"]
    search_help_text = "Rechercher via le numéro du client ou le nom du livre"
    save_on_top = True




admin.site.register(PhysicEbookCmd, PhysicEbookCmdAdmin)
admin.site.register(EbookModel, EbookAdmin)
admin.site.register(SaleEbook, SaleEbookAdmin)
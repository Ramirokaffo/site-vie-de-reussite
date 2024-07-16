from django.contrib import admin
from django.utils.html import format_html

from .models import Formation, FormationVideo, VideoComment, SaleFormation, PhysicFormationCmd

class FormationVideoInline(admin.StackedInline):
    model = FormationVideo


class FormationAdmin(admin.ModelAdmin):
    inlines = [
        FormationVideoInline,
    ]

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
    list_filter = ["category", "published"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["category"]
    search_fields = ["title", "subtitle", "category__name"]
    search_help_text = "Rechercher une formation via son titre, sous-titre ou sa catégorie"
    save_on_top = True
    
    
    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les formations selectionnées")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les formations selectionnées")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)



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

    list_display = ("title", "formation", "published", "order", "created_at", "vdeo")
    list_editable = ("published", "order")
    list_filter = ["published", "formation"]
    search_fields = ["title", "formation__title"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["formation"]
    search_help_text = "Rechercher une vidéo de formation via son titre, ou le nom de la formation"
    save_on_top = True

    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les vidéos sélectionnées")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les vidéos selectionnées")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)




class VideoCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "published", "created_at", "video", "author")
    list_editable = ("published", )

    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les commentaires selectionnés")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les vidéos selectionnés")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)




class SaleFormationAdmin(admin.ModelAdmin):
    list_display = ("formation", "user", "isPaid", "amount", "status", "created_at")

    list_filter = ["isPaid", "formation", "status", "user"]
    search_fields = ["user__firstname", "user__lastname", "formation__title"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["formation", "user"]
    search_help_text = "Rechercher la commande via le nom du client ou le nom de la formation"
    save_on_top = True



class PhysicFormationCmdAdmin(admin.ModelAdmin):
    list_display = ("formation", "phone_number", "isPaid", "amount", "created_at")

    list_filter = ["isPaid", "formation"]
    search_fields = ["phone_number", "formation__title"]
    date_hierarchy = "created_at"
    autocomplete_fields = ["formation"]
    search_help_text = "Rechercher la commande via le numéro du client ou le nom de la formation"
    save_on_top = True



admin.site.register(Formation, FormationAdmin)
admin.site.register(SaleFormation, SaleFormationAdmin)
admin.site.register(FormationVideo, FormationVideoAdmin)
admin.site.register(VideoComment, VideoCommentAdmin)
admin.site.register(PhysicFormationCmd, PhysicFormationCmdAdmin)

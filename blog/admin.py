from django.contrib import admin
from .models import BlogPost, BlogComment
from django.utils.html import format_html

class BlogPostAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        # Obtenez le formulaire par défaut
        form = super().get_form(request, obj, **kwargs)

        # Pré-remplir le champ d'auteur avec l'utilisateur connecté
        form.base_fields['author'].initial = request.user

        # Renvoyer le formulaire modifié
        return form
    
    def illustration_img(self, obj):
        try:
            obj.illustration_image.url
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.illustration_image.url))
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "published", "created_at", "last_updated", "author", "illustration_img", )
    list_editable = ("published", )
    date_hierarchy = "created_at"
    exclude = ["slug"]
    list_filter = ["category", "author", "published"]
    radio_fields = {"category": admin.HORIZONTAL}
    autocomplete_fields = ["category", "author"]
    save_as = True
    save_on_top = True
    search_fields = ["title", "subtitle", "category__name"]
    search_help_text = "Rechercher une publication via son titre, sous-titre ou sa catégorie"
    # search_fields = ["category"]
    # view_on_site = True

    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les publications selectionnées")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les publications selectionnées")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)


    


class BlogCommentAdmin(admin.ModelAdmin):

    list_display = ("content", "published", "created_at", "post", "author")
    list_editable = ("published", )

    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les commentaires selectionnés")
    def make_published(self, request, queryset):
        queryset.update(published=True)



    @admin.action(description="Ne pas publier les commentaires selectionnés")
    def make_no_published(self, request, queryset):
        queryset.update(published=False)




admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)


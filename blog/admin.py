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


class BlogCommentAdmin(admin.ModelAdmin):

    list_display = ("content", "published", "created_at", "post", "author")
    list_editable = ("published", )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)


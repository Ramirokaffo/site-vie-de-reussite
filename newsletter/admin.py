from django.contrib import admin
from bolda.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils.html import strip_tags

from .models import *



class SubscribersAdmin(admin.ModelAdmin):

    list_display = ("email", "is_subscrib", "first_name", "last_name", "last_updated", "created_at",)
    list_filter = ["is_subscrib"]
    date_hierarchy = "created_at"
    search_fields = ["email", "first_name", "last_name"]
    search_help_text = "Rechercher un abonné via son nom, prénom ou son email"
    save_on_top = True
    
    
    # actions = ["make_published", "make_no_published"]

    # @admin.action(description="Publier les formations selectionnées")
    # def make_published(self, request, queryset):
    #     queryset.update(published=True)



    # @admin.action(description="Ne pas publier les formations selectionnées")
    # def make_no_published(self, request, queryset):
    #     queryset.update(published=False)




class SubscribersGroupAdmin(admin.ModelAdmin):

    list_display = ("name", "created_at",)
    date_hierarchy = "created_at"
    search_fields = ["name"]
    search_help_text = "Rechercher un groupe d'abonné via son nom"
    
    
    # actions = ["make_published", "make_no_published"]

    # @admin.action(description="Publier les formations selectionnées")
    # def make_published(self, request, queryset):
    #     queryset.update(published=True)



    # @admin.action(description="Ne pas publier les formations selectionnées")
    # def make_no_published(self, request, queryset):
    #     queryset.update(published=False)




class NewsLetterAdmin(admin.ModelAdmin):

    list_display = ("object", "created_at",)
    date_hierarchy = "created_at"
    search_fields = ["object"]
    search_help_text = "Rechercher un message de diffusion via son objet"
    
    
    actions = ["make_diffuse"]

    @admin.action(description="Diffuser les messages selectionnées")
    def make_diffuse(self, request, queryset):
        # for new in queryset:

        #     plain_message = strip_tags(new.content)
        #     email_list = [subscriber.email for subscriber in new.subscribers.all()]
        #     for subscribers_group in new.subscribers_group.all():

        #         email_list += [subscriber.email for subscriber in subscribers_group]
        for newsletter in queryset:
            email_list = []
            plain_message = strip_tags(newsletter.content)

            # Add emails from subscribers field
            for subscriber in newsletter.subscribers.all():
                email_list.append(subscriber.email)

            # Add emails from subscribers_group field (use .all() to query)
            for group in newsletter.subscribers_group.all():
                for subscriber in group.subscribers.all():
                    email_list.append(subscriber.email)
                send_mail(
            subject=newsletter.object,
            message=plain_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=email_list,
            html_message=newsletter.content,
            fail_silently=True
            )
        self.message_user(request, message="Message diffusé avec succès.")
            



    # @admin.action(description="Ne pas publier les formations selectionnées")
    # def make_no_published(self, request, queryset):
    #     queryset.update(published=False)











admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(SubscribersGroup, SubscribersGroupAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
# admin.site.register(VideoComment, VideoCommentAdmin)

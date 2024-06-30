from django.db import models
from tinymce.models import HTMLField

class Subscribers(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="nom")
    last_name = models.CharField(max_length=255, verbose_name="prénom")
    email = models.EmailField(max_length=50, blank=False, unique=True, null=False, verbose_name="email")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date de publication")
    is_subscrib = models.BooleanField(default=True, verbose_name="abonné(e)")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "abonné"
        verbose_name_plural = "abonnés"

    def __str__(self) -> str:
        return self.email
    

class SubscribersGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name="nom du groupe")
    subscribers = models.ManyToManyField(Subscribers, verbose_name="abonné(e)")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date de publication")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "groupe d'abonné"
        verbose_name_plural = "groupes d'abonné"

    def __str__(self) -> str:
        return self.name
    
class NewsLetter(models.Model):
    object = models.CharField(max_length=255, verbose_name="objet")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date de publication")
    content = HTMLField(max_length=5000000, blank=True, verbose_name="message")
    subscribers_group = models.ManyToManyField(
        SubscribersGroup, related_name='subscribers_group', symmetrical=False, blank=True, verbose_name="groupe d'abonné(e)"
    )
    subscribers = models.ManyToManyField(
        Subscribers, related_name='subscribers', symmetrical=False, blank=True, verbose_name='abonné(e)'
    )


    class Meta:
        ordering = ['-created_at']
        verbose_name = "message de diffusion"
        verbose_name_plural = "messages de diffusion"

    def __str__(self) -> str:
        return self.object
    

from django.db import models
from django.contrib.auth.models import User
from core.models import CategoryModel
from tinymce.models import HTMLField
from django.urls import reverse

class EventModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255, unique=True, verbose_name="titre")
    subtitle = models.CharField(blank=False, null=False, default="", max_length=255, verbose_name="texte présentatif")
    description = HTMLField(max_length=5000000, verbose_name="description de la formation")
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="catégorie")
    start_at = models.DateTimeField(blank=False, null=True, verbose_name="date de debut")
    end_at = models.DateTimeField(blank=False, null=True, verbose_name="date de fin")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'ajout")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    published = models.BooleanField(default=True, verbose_name="publié")
    show_at_home = models.BooleanField(default=False, blank=False, null=False, verbose_name="afficher à l'accueil")
    illustration_image = models.ImageField(blank=False, null=False, upload_to='images/events/%Y/%m/%d', verbose_name="image d'illustration")
    illustration_video = models.CharField(max_length=20, blank=True, null=True, verbose_name="Identifiant de la vidéo d'illustration")
    inscription_link = models.CharField(blank=True, null=True, max_length=355, verbose_name="lien d'inscription")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "évènement"
        verbose_name_plural = "évènements"

    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'event_id': self.id})


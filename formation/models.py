from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from core.models import CategoryModel
from tinymce.models import HTMLField
from django.urls import reverse
from django.db.models import Max
from uuid import uuid4


def validate_video_file(value):
    if not value.name.upper().endswith(('.MP4', ".MOV", ".AVI", ".MKV")):
        raise ValidationError("Le fichier doit avoir l'un des formats suivants: MP4, MOV, AVI et MKV")
    

class Formation(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255, unique=True, verbose_name="Titre")
    subtitle = models.CharField(blank=False, null=False, default="", max_length=255, verbose_name="Texte présentatif")
    description = HTMLField(max_length=5000000, verbose_name="description de la formation")
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Catégorie")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'ajout")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    published = models.BooleanField(default=True, verbose_name="Publié")
    illustration_image = models.ImageField(blank=False, null=False, upload_to='images/formation/%Y/%m/%d', verbose_name="Image d'illustration")
    illustration_video = models.CharField(max_length=20, blank=True, null=True, verbose_name="Identifiant de la vidéo d'illustration")
    normal_price = models.FloatField(verbose_name="Prix barré", null=False)
    promo_price = models.FloatField(verbose_name="Prix de vente")
    course_duration = models.IntegerField(verbose_name="Durée totale des cours (en heures)")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"

    def get_absolute_url(self):
        return reverse('formation:detail', kwargs={'formation_id': self.id})

    def get_videos_count(self) -> int:
        return FormationVideo.objects.filter(formation=self).count()

class FormationVideo(models.Model):
    title = models.CharField(unique=False, max_length=255, verbose_name="Titre de la vidéo")
    decription = HTMLField(null=True, blank=True)
    video = models.CharField(max_length=20, blank=True, null=True, verbose_name="Identifiant de la vidéo")
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Formation")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'ajout")
    published = models.BooleanField(default=True, verbose_name="Publié")
    order = models.IntegerField(default=1, blank=False, null=False, verbose_name="Ordre", help_text="Ordre d'affichage de la vidéo", auto_created=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Vidéo de formation"
        verbose_name_plural = "Vidéos de formation"

    def save(self, *args, **kwargs):
        if not self.order:
            current_max_order = self.objects.filter(video=self.video).aggregate(Max("order", default=0)).get("order__max")
            self.order = current_max_order

        super().save(*args, **kwargs)



class VideoComment(models.Model):
    video = models.ForeignKey(FormationVideo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Vidéo")
    content = models.TextField(max_length=200, verbose_name="Contenu", null=False, blank=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True)
    published = models.BooleanField(default=True, verbose_name="Publié")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
    replies = models.ManyToManyField(
        'self', related_name='responses', symmetrical=False, blank=True
    )

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = "commentaire de vidéo"
        verbose_name_plural = "commentaires de vidéo"


class SaleFormation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="acheté par")
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="formation achetée")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="date d'achat")
    isPaid = models.BooleanField(default=False, verbose_name="payé ?")
    amount = models.FloatField(blank=False, null=False, verbose_name="montant facturé")
    my_reference = models.CharField(max_length=255, blank=False, null=False, verbose_name="reference de la transaction", default=uuid4)
    notch_pay_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="reference de notchpay")
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name="status du paiement")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    
    def __str__(self):
        return f"{self.user} - {self.formation}"
    
    class Meta:
        verbose_name = "formation achetée"
        verbose_name_plural = "formations achetées"



class PhysicFormationCmd(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="formation achetée")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="date de commande")
    isPaid = models.BooleanField(default=False, verbose_name="payé?")
    amount = models.FloatField(blank=False, null=False, verbose_name="montant facturé")
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Téléphone client")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    
    def __str__(self):
        return f"{self.phone_number} - {self.formation}"
    
    class Meta:
        verbose_name = "commande physique"
        verbose_name_plural = "commandes physiques"


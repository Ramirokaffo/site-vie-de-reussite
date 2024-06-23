from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from core.models import CategoryModel
from tinymce.models import HTMLField
from django.urls import reverse
import uuid


def validate_video_file(value):
    if not value.name.upper().endswith(('.MP4', ".MOV", ".AVI", ".MKV")):
        raise ValidationError("Le fichier doit avoir l'un des formats suivants: MP4, MOV, AVI et MKV")
    


def validate_pdf_file(value):
    if not value.name.upper().endswith(('.PDF')):
        raise ValidationError("Le fichier doit être au format pdf")
    
 

class EbookModel(models.Model):
    AVAILIBILITY_TYPE = (
        ("numeric", "Uniquement la version physique", ),
        ("physic", "Uniquement la version numérique", ),
        ("both", "Version physique et numerique disponibles",),
        )

    title = models.CharField(max_length=255, unique=True, verbose_name="titre du livre")
    subtitle = models.CharField(max_length=255, blank=False, default="", null=False, verbose_name="Texte présentatif")
    description = HTMLField(max_length=5000000, verbose_name="description du livre")
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Catégorie du livre")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'ajout")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    ebook_file = models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', validators=[validate_pdf_file], verbose_name="Livre au format pdf")
    illustration_image = models.ImageField(blank=True, null=True, upload_to='images/ebook/%Y/%m/%d', verbose_name="Image d'illustration")
    illustration_video = models.CharField(blank=True, null=True, max_length=20, verbose_name="identifiant vers la vidéo d'illustration")
    normal_price = models.FloatField(verbose_name="prix barré", null=False)
    promo_price = models.FloatField(verbose_name="prix de vente/facturé")
    published = models.BooleanField(default=True, verbose_name="publié")
    availability = models.CharField(max_length=10, choices=AVAILIBILITY_TYPE, verbose_name="version disponible", default="both")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "e-book"
        verbose_name_plural = "e-books"

    def get_absolute_url(self):
        return reverse('ebook:detail', kwargs={'ebook_id': self.id})




class SaleEbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="acheté par")
    ebook = models.ForeignKey(EbookModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="livre acheté")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="date d'achat")
    isPaid = models.BooleanField(default=False, verbose_name="payé ?")
    amount = models.FloatField(blank=False, null=False, verbose_name="montant facturé")
    my_reference = models.CharField(max_length=255, blank=False, null=False, verbose_name="reference de la transaction", default=uuid.uuid4)
    notch_pay_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="reference de notchpay")
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name="le status du paiement")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    
    def __str__(self):
        return f"{self.user} - {self.ebook}"
    
    class Meta:
        verbose_name = "livre vendu"
        verbose_name_plural = "livres vendus"





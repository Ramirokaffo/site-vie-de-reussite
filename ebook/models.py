from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from core.models import CategoryModel
from tinymce.models import HTMLField


def validate_video_file(value):
    if not value.name.upper().endswith(('.MP4', ".MOV", ".AVI", ".MKV")):
        raise ValidationError("Le fichier doit avoir l'un des formats suivants: MP4, MOV, AVI et MKV")
    


def validate_pdf_file(value):
    if not value.name.upper().endswith(('.PDF')):
        raise ValidationError("Le fichier doit être au format pdf")
    

# class EbookCategory(models.Model):
#     name = models.CharField(max_length=255, unique=True, verbose_name="Nom")
#     description = models.TextField(blank=True, null=True, verbose_name="description")
#     last_updated = models.DateTimeField(auto_now=True)
#     created_at = models.DateField(blank=True, null=True)

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = "Catégorie de livre"
#         verbose_name_plural = "Catégories de livre"

#     def __str__(self) -> str:
#         return self.name
   

class EbookModel(models.Model):
    AVAILIBILITY_TYPE = (
        ("numeric", "Uniquement la version physique", ),
        ("physic", "Uniquement la version numérique", ),
        ("both", "Version physique et numerique disponibles",),
        )

    title = models.CharField(max_length=255, unique=True, verbose_name="Titre du livre")
    subtitle = models.CharField(max_length=255, blank=False, default="", null=False, verbose_name="Texte présentatif")
    description = HTMLField(max_length=5000000, verbose_name="description du livre")
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Catégorie du livre")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'ajout")
    ebook_file = models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', validators=[validate_pdf_file], verbose_name="Livre au format pdf")
    illustration_image = models.ImageField(blank=True, null=True, upload_to='images/ebook/%Y/%m/%d', verbose_name="Image d'illustration")
    illustration_video = models.CharField(blank=True, null=True, max_length=20, verbose_name="Identifiant vers la vidéo d'illustration")
    normal_price = models.FloatField(verbose_name="Prix normal du livre", null=False)
    promo_price = models.FloatField(verbose_name="Prix promotionnel")
    published = models.BooleanField(default=True, verbose_name="Publié")
    availability = models.CharField(max_length=10, choices=AVAILIBILITY_TYPE, verbose_name="Version disponible", default="both")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "E-book"
        verbose_name_plural = "E-books"




class SaleEbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Acheté par")
    ebook = models.ForeignKey(EbookModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Livre acheté")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date d'achat")
    isPaid = models.BooleanField(default=False, verbose_name="Payé ?")
    amount = models.FloatField(blank=False, null=False, verbose_name="Montant facturé")

    def __str__(self):
        return f"{self.user} - {self.ebook}"
    
    class Meta:
        verbose_name = "Livre vendu"
        verbose_name_plural = "Livres vendus"





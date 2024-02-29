from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True, verbose_name="Nom")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie d'élément"
        verbose_name_plural = "Catégories d'éléments"
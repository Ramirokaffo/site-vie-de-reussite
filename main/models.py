from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True, verbose_name="Nom")
#     description = models.TextField(blank=True, verbose_name="description")
#     last_updated = models.DateTimeField(auto_now=True)
#     created_at = models.DateField(blank=True, null=True)

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = "Catégorie de formation"

#     def __str__(self) -> str:
#         return self.name
   

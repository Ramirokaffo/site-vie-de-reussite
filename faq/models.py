from django.db import models

from django.contrib.auth.models import User
from core.models import CategoryModel


# class FaqCategory(models.Model):
#     name = models.CharField(max_length=255, unique=True, verbose_name="Nom")
#     description = models.TextField(blank=True, verbose_name="description")
#     last_updated = models.DateTimeField(auto_now=True)
#     created_at = models.DateField(blank=True, null=True)

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = "Catégorie de question"
#         verbose_name_plural = "Catégories de question"

#     def __str__(self) -> str:
#         return self.name



class FaqModel(models.Model):

    FAQ_CATEGORY = (
        ("formation", "Formation", ),
        ("ebook", "Livres", ),
        ("about", "À propos de l'activité",),
        )

    question = models.CharField(max_length=255, unique=True, verbose_name="question")
    answer = models.TextField(blank=True, verbose_name="réponse")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    category = models.CharField(choices=FAQ_CATEGORY, verbose_name="Catégorie de Faq", max_length=20)
    # faq_category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="catégorie")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Foire aux questions"

    def __str__(self) -> str:
        return self.question
    

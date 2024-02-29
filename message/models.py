from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nom du visiteur")
    email = models.EmailField(blank=True, verbose_name="Adresse mail du visiteur")
    created_at = models.DateField(blank=True, null=True, auto_now=True)
    content = models.TextField(max_length=255, blank=False, null=False, verbose_name="Contenu du message")

    class Meta:
        verbose_name = "Message d'un visiteur"
        verbose_name_plural = "Messages des visiteurs"

    def __str__(self) -> str:
        return self.content[:50]
    

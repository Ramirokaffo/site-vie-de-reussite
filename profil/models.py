from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfilModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="propriétaire du profil")
    # is_visible = models.BooleanField(default=False, null=False, blank=False, verbose_name="Est-ce visible sur le site ?")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, auto_now=True, null=True, verbose_name="créé le")
    profil_image = models.ImageField(blank=True, null=True, upload_to='images/profil', verbose_name="photo de profil")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "profil utilisateur"
        verbose_name_plural = "profils des utilisateurs"
    
    # def save(self, *args, **kwargs):
    #     self.last_updated = timezone.now()
    #     super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.user)
    


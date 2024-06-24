from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from profil.models import UserProfilModel

class TestimonyModel(models.Model):
    RATE_LEVEL = (
        (0, "Très mécontent", ),
        (1, "Mécontent", ),
        (2, "Indifférent",),
        (3, "Satisfait",),
        (4, "Très Satisfait",),
        )
    content = models.TextField(blank=False, null=False, verbose_name="contenu", max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="auteur du témoignage")
    is_visible = models.BooleanField(default=False, null=False, blank=False, verbose_name="est-ce visible sur le site ?")
    last_updated = models.DateTimeField(auto_now_add=True, verbose_name="modifié le")
    created_at = models.DateField(blank=True, auto_now=True, null=True, verbose_name="créé le")
    rate = models.CharField(max_length=10, choices=RATE_LEVEL, verbose_name="note", default=4)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "témoignage"
        verbose_name_plural = "témoignages"
    
    def save(self, *args, **kwargs):
        self.last_updated = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.content[:100] + "..."
    
    def get_user_profil(self):
        return UserProfilModel.objects.get(user=self.author)

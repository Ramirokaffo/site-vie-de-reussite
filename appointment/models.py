from django.db import models
 

class AppointmentModel(models.Model):
    GENDER_TYPE = (
        ("H", "Homme", ),
        ("F", "Femme"),
        ("A", "Aucun",),
        )
    full_name = models.CharField(blank=False, null=False, max_length=255, verbose_name="nom complet")
    phone_number = models.CharField(blank=False, null=False, default="", max_length=255, verbose_name="téléphone")
    objectif = models.TextField(blank=False, null=False, verbose_name="onjectif de la réunion")
    country = models.CharField(blank=False, null=True, max_length=255, verbose_name="pays")
    city = models.CharField(blank=False, null=True, max_length=255, verbose_name="ville")
    email = models.CharField(blank=False, null=True, max_length=255, verbose_name="email")
    gender = models.CharField(blank=False, null=True, max_length=2, default="H", verbose_name="sexe", choices=GENDER_TYPE)
    my_date = models.DateField(blank=False, null=True, verbose_name="date du rendez-vous")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="date d'ajout")
    
    def __str__(self):
        return self.objectif[:50] + "..."
    
    class Meta:
        verbose_name = "rendez-vous"
        verbose_name_plural = "rendez-vous"



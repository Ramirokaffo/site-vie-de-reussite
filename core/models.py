from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True, verbose_name="Nom")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie d'élément"
        verbose_name_plural = "Catégories d'éléments"


class SiteVideoModel(models.Model):
    SHOW_WHERE_TYPE = (
        ("home", "Accueil", ),
        ("formations", "Formations"),
        ("formation", "Détails des formations"),
        ("ebooks", "Ebooks",),
        ("ebook", "Détails des ebooks",),
        ("events", "Évènements",),
        ("event", "Détail des évènements",),
        ("faq", "Foire aux questions",),
        ("about", "À propos",),
        ("blog", "Blog",),
        ("post", "Post",),
        )
        
    title = models.CharField(max_length=255, null=True, unique=True, verbose_name="titre de la vidéo")
    video = models.CharField(max_length=255, null=True, unique=True, verbose_name="identifiant YouTube de la vidéo")
    show_where = models.CharField(blank=False, null=False, max_length=15, default="home", verbose_name="afficher où ?", choices=SHOW_WHERE_TYPE)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    published = models.BooleanField(default=True, verbose_name="publié")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "vidéo du site"
        verbose_name_plural = "vidéos du site"





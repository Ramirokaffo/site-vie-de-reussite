from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from core.models import CategoryModel
from tinymce.models import HTMLField



class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    subtitle = models.CharField(max_length=255, blank=False, default="", null=False, verbose_name="Texte présentatif")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur de la publication")
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Catégorie de la publication")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="Date de publication")
    published = models.BooleanField(default=True, verbose_name="Publié")
    content = HTMLField(max_length=5000000, blank=True, verbose_name="Contenu")
    illustration_image = models.ImageField(blank=True, null=True, upload_to='images/post/%Y/%m/%d', verbose_name="Image d'illustration")
    

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)



class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Publication")
    content = models.TextField(max_length=200, verbose_name="Contenu")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True)
    published = models.BooleanField(default=True, verbose_name="Publié")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
    replies = models.ManyToManyField(
        'self', related_name='responses', symmetrical=False, blank=True
    )

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = "Commentaire de post"
        verbose_name_plural = "Commentaires de post"



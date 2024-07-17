from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from core.models import CategoryModel
from tinymce.models import HTMLField
from django.urls import reverse
from profil.models import UserProfilModel
from ebook.models import EbookModel
from formation.models import Formation

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="titre")
    subtitle = models.CharField(max_length=255, blank=False, default="", null=False, verbose_name="texte présentatif")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="auteur de la publication")
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name="catégorie de la publication")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True, verbose_name="date de publication")
    published = models.BooleanField(default=True, verbose_name="publié")
    content = HTMLField(max_length=5000000, blank=True, verbose_name="contenu")
    illustration_image = models.ImageField(blank=True, null=True, upload_to='images/post/%Y/%m/%d', verbose_name="image d'illustration")
    high_light_ebooks = models.ManyToManyField(
        EbookModel, related_name='high_light_ebooks', symmetrical=False, blank=True, verbose_name='livres mis en avant'
    )
    high_light_formations = models.ManyToManyField(
        Formation, related_name='high_light_formations', symmetrical=False, blank=True, verbose_name='formations mis en avant'
    )


    class Meta:
        ordering = ['-created_at']
        verbose_name = "publication"
        verbose_name_plural = "publications"

    def __str__(self) -> str:
        return self.title
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'post_id': self.id})



class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="publication")
    content = models.TextField(max_length=500, verbose_name="contenu")
    created_at = models.DateTimeField(blank=True, null=True, auto_created=True, auto_now_add=True)
    published = models.BooleanField(default=True, verbose_name="publié")
    author = models.ForeignKey(UserProfilModel, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="auteur")
    reply_of = models.ForeignKey("self",  blank=True, null=True, on_delete=models.SET_NULL, verbose_name="réponse de")

    # replies = models.ManyToManyField(
    #     'self', related_name='responses', symmetrical=False, blank=True
    # )

    def __str__(self):
        # self.author.get_full_name
        return self.content
    
    class Meta:
        verbose_name = "commentaire de post"
        verbose_name_plural = "commentaires de post"

    def get_replies(self):
        replies = BlogComment.objects.filter(reply_of=self)
        return replies

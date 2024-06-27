from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from core.models import CategoryModel
from tinymce.models import HTMLField
from django.urls import reverse
from profil.models import UserProfilModel

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    subtitle = models.CharField(max_length=255, blank=False, default="", null=False, verbose_name="Texte présentatif")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur de la publication")
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name="Catégorie de la publication")
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

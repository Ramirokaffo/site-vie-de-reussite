from django.urls import path
from .sitemaps import BlogPostSitemap
from django.contrib.sitemaps.views import sitemap

from .views import index, detail

sitemaps = {
    "bolg": BlogPostSitemap,

}

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("<int:post_id>/", detail, name="detail"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap")
]
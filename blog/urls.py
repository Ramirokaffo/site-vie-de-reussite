from django.urls import path
from .sitemaps import BlogPostSitemap
from django.contrib.sitemaps.views import sitemap

from .views import index, detail, comment, reply

sitemaps = {
    "bolg": BlogPostSitemap,

}

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("comment/<int:post_id>/", comment, name="comment"),
    path("reply/<int:comment_id>/", reply, name="reply"),
    path("<int:post_id>/", detail, name="detail"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap")
]
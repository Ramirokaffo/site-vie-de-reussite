"""
URL configuration for bolda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings 
from django.urls import re_path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from bolda.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogPostSitemap
from ebook.sitemaps import EbookSitemap
from event.sitemaps import EventSitemap
from formation.sitemaps import FormationSitemap
# from django.conf.urls import patterns

sitemaps = {
    'static': StaticViewSitemap,
    "blog": BlogPostSitemap,
    "ebook": EbookSitemap,
    "event": EventSitemap,
    "formation": FormationSitemap,

}

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
google_analytic_view = RedirectView.as_view(url='/static/google955276c8e840c68a.html', permanent=True)

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("legal-notice/", views.legal_notice, name="legal_notice"),
    path("get_images_url/", views.get_images_url, name="get_images_url"),
    path("web_hooks_end_point/", views.web_hooks_end_point, name="web_hooks_end_point"),
    path("delete_migrations_files/", views.delete_migrations_files, name="delete_migrations_files"),
    path("blog/", include("blog.urls")),
    path("ebook/", include("ebook.urls")),
    path("formation/", include("formation.urls")),
    path("faq/", include("faq.urls")),
    path("event/", include("event.urls")),
    path("profil/", include("profil.urls")),
    path("auth/", include("authentification.urls")),
    path("message/", include("message.urls")),
    path("testimony/", include("testimony.urls")),
    path("appointment/", include("appointment.urls")),
    path("newsletter/", include("newsletter.urls")),
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', favicon_view),
    re_path(r'^google955276c8e840c68a\.html$', google_analytic_view),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", include("blog.urls")),
    path("ebook/", include("ebook.urls")),
    path("formation/", include("formation.urls")),
    path("faq/", include("faq.urls")),
    path("event/", include("event.urls")),
    path("profil/", include("profil.urls")),
    path("auth/", include("authentification.urls")),
    path("message/", include("message.urls")),
    path("appointment/", include("appointment.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

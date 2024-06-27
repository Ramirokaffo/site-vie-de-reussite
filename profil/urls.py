
from django.urls import path

from .views import index, formation, ebook, detail, update

app_name = "profil"
urlpatterns = [
    path("", index, name="index"),
    path("formation", formation, name="formation"),
    path("ebook", ebook, name="ebook"),
    path("update", update, name="update"),
    path("formation/<int:formation_id>/", detail, name="detail"),
]

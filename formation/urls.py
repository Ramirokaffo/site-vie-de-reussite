
from django.urls import path

from .views import index, detail, comment

app_name = "formation"
urlpatterns = [
    path("", index, name="index"),
    path("comment", comment, name="comment"),
    path("<int:formation_id>/", detail, name="detail"),
]

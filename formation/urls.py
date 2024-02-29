
from django.urls import path

from .views import index, detail

app_name = "formation"
urlpatterns = [
    path("", index, name="index"),
    path("<int:formation_id>/", detail, name="detail"),
]

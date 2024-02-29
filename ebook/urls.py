
from django.urls import path

from .views import index, detail

app_name = "ebook"
urlpatterns = [
    path("", index, name="index"),
    path("<int:ebook_id>/", detail, name="detail"),
]

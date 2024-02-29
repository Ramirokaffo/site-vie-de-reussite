
from django.urls import path

from .views import index

app_name = "faq"
urlpatterns = [
    path("", index, name="index"),
    # path("<int:formation_id>/", detail, name="detail"),
]

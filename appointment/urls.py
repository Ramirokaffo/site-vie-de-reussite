
from django.urls import path

from .views import add

app_name = "appointment"
urlpatterns = [
    path("add", add, name="add"),
]

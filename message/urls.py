
from django.urls import path

from .views import add

app_name = "message"
urlpatterns = [
    path("add", add, name="add"),
]

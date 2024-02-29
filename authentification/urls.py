
from django.urls import path

from .views import index, register

app_name = "auth"
urlpatterns = [
    path("login", index, name="login"),
    path("register", register, name="register"),
]

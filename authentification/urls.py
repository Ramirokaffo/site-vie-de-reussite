
from django.urls import path

from .views import index, register, log_out

app_name = "auth"
urlpatterns = [
    path("login", index, name="login"),
    path("register", register, name="register"),
    path("logout", log_out, name="logout"),
]

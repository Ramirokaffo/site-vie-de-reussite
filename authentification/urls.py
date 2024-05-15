
from django.urls import path

from .views import index, register, log_out, activate, authMail

app_name = "auth"
urlpatterns = [
    path("login", index, name="login"),
    path("register", register, name="register"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("authMail", authMail, name="authMail"),
    path("logout", log_out, name="logout"),
]

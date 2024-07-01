
from django.urls import path

from .views import *

app_name = "auth"
urlpatterns = [
    path("login", index, name="login"),
    path("register", register, name="register"),
    path("reset", reset, name="reset"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("reset_pwd/<uidb64>/<token>", reset_pwd, name="reset_pwd"),
    path("new_password/<uidb64>", new_password, name="new_password"),
    path("authMail", authMail, name="authMail"),
    path("logout", log_out, name="logout"),
]

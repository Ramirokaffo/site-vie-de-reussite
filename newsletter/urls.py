
from django.urls import path

from .views import *

app_name = "newsletter"
urlpatterns = [
    path("subscribe", subscribe, name="subscribe"),
    path("unsubscribe", unsubscribe, name="unsubscribe"),


]


from django.urls import path

from .views import create

app_name = "testimony"
urlpatterns = [
    path("create", create, name="create"),


]

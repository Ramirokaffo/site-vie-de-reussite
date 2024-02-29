from django.urls import path

from .views import index, detail, results

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("<int:post_id>/", detail, name="detail"),

]
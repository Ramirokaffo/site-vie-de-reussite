
from django.urls import path

from .views import index, detail, buy, ebook_buy_callback

app_name = "ebook"
urlpatterns = [
    path("", index, name="index"),
    path("ebook_buy_callback/", ebook_buy_callback, name="ebook_buy_callback"),
    path("buy/<int:ebook_id>/", buy, name="buy"),
    path("<int:ebook_id>/", detail, name="detail"),
]

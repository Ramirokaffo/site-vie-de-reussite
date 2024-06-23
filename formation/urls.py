
from django.urls import path

from .views import index, detail, comment, buy, formation_buy_callback

app_name = "formation"
urlpatterns = [
    path("", index, name="index"),
    path("comment", comment, name="comment"),
    path("<int:formation_id>/", detail, name="detail"),
    path("buy/<int:formation_id>/", buy, name="buy"),
    path("formation_buy_callback/", formation_buy_callback, name="formation_buy_callback"),
    

]

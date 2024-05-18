from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = "Administration du site vie de réussite"
    
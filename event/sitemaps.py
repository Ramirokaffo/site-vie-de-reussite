from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models  import EventModel


class EventSitemap(Sitemap):
    
    def items(self):
        return EventModel.objects.filter(published=True)
    
    def lastmod(self, obj):
        return obj.last_updated
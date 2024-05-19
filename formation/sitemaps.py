from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models  import Formation


class FormationSitemap(Sitemap):
    
    def items(self):
        return Formation.objects.filter(published=True)
    
    def lastmod(self, obj):
        return obj.last_updated
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models  import EbookModel


class EbookSitemap(Sitemap):
    
    def items(self):
        return EbookModel.objects.filter(published=True)
    
    def lastmod(self, obj):
        return obj.last_updated
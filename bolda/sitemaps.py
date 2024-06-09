from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['index', "privacy", "legal_notice", "event:index", "blog:index", "formation:index", "ebook:index", "faq:index"]
    
    def location(self, item):
        return reverse(item)
    

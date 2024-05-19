from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models  import BlogPost


class BlogPostSitemap(Sitemap):
    
    def items(self):
        return BlogPost.objects.filter(published=True)
    
    def lastmod(self, obj):
        return obj.last_updated
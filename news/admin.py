from django.contrib import admin
from .models import NewsArticle

# Register your models here.


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['get_source_name', 'title', 'published_at']
    search_fields = ['get_source_name', 'title']

    def get_source_name(self, obj):
        return obj.sources.get('name')

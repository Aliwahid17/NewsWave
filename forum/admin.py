from django.contrib import admin
from .models import CommunityForums

# Register your models here.


@admin.register(CommunityForums)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at", "votes", "creator_name"]
    search_fields=["title", "published_at", "votes"]
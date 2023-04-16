from django.contrib import admin
from .models import Community_Forums, Forums_Votes, Comments

# Register your models here.


@admin.register(Community_Forums)
class CommunityForumsAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at", "votes", "creator_name"]
    search_fields = ["title", "published_at", "votes"]


@admin.register(Forums_Votes)
class Vote_CategoryAdmin(admin.ModelAdmin):
    list_display = ["user", "forum", "vote"]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "comment", "published_at"]

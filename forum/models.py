from django.db import models
from uuid import uuid4
from django.db.models.signals import pre_save
from django.dispatch import receiver
from user.models import Profile
from math import ceil

# Create your models here.

class CommunityForums(models.Model):
    title = models.TextField(blank=False)
    uuid = models.UUIDField(unique=True, auto_created=True, default=uuid4)
    description = models.CharField(blank=False , max_length=600)
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.JSONField(default=list)
    votes = models.IntegerField()
    creator_name = models.TextField(blank=False)
    creator_image = models.URLField()

    class Meta:
        verbose_name_plural = "Community Forums"


@receiver(pre_save , sender=CommunityForums)
def delete_community_forum(sender, instance, **kwargs):
    total_user = ceil(Profile.objects.count() * 51 / 100)
    total_votes = abs(instance.votes)
    if instance.votes < 0:
        if total_votes > total_user:
            instance.delete()

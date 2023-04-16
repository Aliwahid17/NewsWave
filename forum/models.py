from django.db import models
from uuid import uuid4
from django.db.models.signals import pre_save 
from django.dispatch import receiver
from user.models import Profile
from math import ceil

# Create your models here.


class Community_Forums(models.Model):
    title = models.TextField(blank=False)
    uuid = models.UUIDField(unique=True, auto_created=True, default=uuid4)
    description = models.CharField(blank=False, max_length=600)
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.JSONField(default=list)
    votes = models.IntegerField()
    creator_email= models.EmailField()
    creator_name = models.TextField(blank=False)
    creator_image = models.URLField()
    user_votes = models.ManyToManyField(
        Profile, through="Forums_Votes", related_name="User")

    class Meta:
        verbose_name_plural = "Community Forums"



# @receiver(pre_save, sender=Community_Forums)
# def update_community_forum(sender, instance, **kwargs):
#     print(instance)
    # # Check if the votes field has changed
    # if instance.pk is not None:
    #     old_instance = sender.objects.get(pk=instance.pk)
    #     if old_instance.votes != instance.votes:
    #         # Update the votes field and save the instance
    #         # instance.votes = votes
    #         instance.save()
    #         # Trigger the delete_community_forum function
    #         delete_community_forum(sender, instance, **kwargs)

# @receiver(pre_save, sender=Community_Forums)
# def delete_community_forum(sender, instance, **kwargs):
#     print("f",instance)
#     total_user = round(Profile.objects.count() * 51 / 100)
#     total_votes = abs(instance.votes)
#     if instance.votes < 0:
#         if total_votes > total_user:
#             instance.delete()


class Forums_Votes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    forum = models.ForeignKey(Community_Forums, on_delete=models.CASCADE)
    vote = models.TextField(default="No")

    class Meta:
        verbose_name_plural = "Forums Votes"


class Comments(models.Model):
    post = models.ForeignKey(Community_Forums, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile , on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

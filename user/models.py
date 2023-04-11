from django.db import models
from allauth.socialaccount.models import SocialAccount

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
    DOB=models.DateField(blank=False)
    country=models.CharField(blank=False , max_length=50)
    categories=models.JSONField(default=list,editable=True)
    sources=models.JSONField(default=list,editable=True)

    class Meta:
        ordering = ["user__user__date_joined" , 'user__user__last_login']
        verbose_name_plural = "Profiles"

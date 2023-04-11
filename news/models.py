from django.db import models
from user.models import Profile
# from allauth.socialaccount.models import SocialAccount
# Create your models here.


class NewsArticle(models.Model):

    sources = models.JSONField(default=dict, editable=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    url = models.URLField(max_length=200)
    url_to_image = models.URLField(max_length=200)
    published_at = models.DateTimeField()
    content = models.CharField(max_length=300)
    likes = models.ManyToManyField(Profile, related_name="Likes")
    comments = models.ManyToManyField(Profile,related_name="Comments")
    saved = models.ManyToManyField(Profile,related_name='Saved')


    class Meta:
        verbose_name_plural = "NewsArticles"
    

    def likesCount(self):
        return self.likes.count()

    def userLiked(self,email):
        like = ''
        if self.likes.filter(user__user__email=email):
            like = 'is-active'
        
        return like
    
    def userSaved(self,email):
        s = ''
        if self.s.filter(user__user__email=email):
            s = 'saved'
        
        return s
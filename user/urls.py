from django.urls import path
from .views import new_user , user_profile

urlpatterns = [
    path("new/" , new_user , name="new_user"),
    path('profile/' , user_profile , name="user_profile")
]

from django.urls import path
from .views import new_user

urlpatterns = [
    path("new/" , new_user , name="new_user")
]

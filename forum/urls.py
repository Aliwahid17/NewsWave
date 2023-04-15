from django.urls import path
from .views import forum_home , create_forum

urlpatterns = [
    path('', forum_home, name="forum_home"),
    path('create/',create_forum , name="create_forum")
]

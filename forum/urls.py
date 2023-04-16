from django.urls import path
from .views import forum_home, create_forum , forum_view

urlpatterns = [
    path('', forum_home, name="forum_home"),
    path('create/', create_forum, name="create_forum"),
    path('<uuid:uuid>/' , forum_view , name="forum_view")
]

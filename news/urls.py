from django.urls import path
from .views import home , trending

urlpatterns = [
    path('', home, name="home"),
    path('trending', trending, name="trending"),
]

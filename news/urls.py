from django.urls import path
from .views import home

urlpatterns = [
    # path('', Home.as_view(), name="home"),
    path('', home, name="home"),
]

from django.shortcuts import render
from django.views.generic import TemplateView
from user.options import news_categories

# Create your views here.




def home(request):
    data = {'news_categories': news_categories}
    return render(request , 'index.html', context=data)

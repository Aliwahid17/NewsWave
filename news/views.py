from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.




def home(request):
    # print(request.user)
    return render(request , 'index.html')
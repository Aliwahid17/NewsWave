from django.shortcuts import render
from django.views.generic import TemplateView
from user.options import news_categories, news_sources_id, news_sources_url, news_sources_dic, news_filter
from .news import carousel_news
from user.models import Profile

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        email = request.user.email
    else:
        email = None

    try:
        user = Profile.objects.filter(user__user__email=email)[0]

        news_id = []
        news_url = []

        for source in user.sources.split(','):
            news_id.append(news_sources_dic[source][0])
            news_url.append(news_sources_dic[source][1])

    except:
        print("Error")

    data = {'news_categories': news_categories if email is None else user.categories.split(','),
            'slide_articles': carousel_news(','.join(news_sources_id), ','.join(news_sources_url)) if email is None else carousel_news(','.join(news_id), ','.join(news_url)),
            "news_sort": news_filter
            }

    return render(request, 'index.html', context=data)


def trending(request):
    return render(request, 'trending.html')

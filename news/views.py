from django.shortcuts import render
from json import dumps, loads, dump, load
from user.options import news_categories, news_sources_id, news_sources_url, news_sources_dic, news_filter
from .news import carousel_news, daily_news
from user.models import Profile
from .models import NewsArticle
from django.http import JsonResponse, HttpResponseNotAllowed


def home(request):

    email = request.user.email if request.user.is_authenticated else None

    if request.method == "POST":
        content = loads(request.body)

        category = content['category']
        sort = content['sort']
        title = content['title']

    try:
        user = Profile.objects.filter(user__user__email=email)[0]
        news_id = []
        news_url = []

        for source in user.sources.split(','):
            news_id.append(news_sources_dic[source][0])
            news_url.append(news_sources_dic[source][1])


    except:
        print("NO USER")

    # Test Code #

    # with open('news.json', 'r') as f:
    #     daily_new = load(f)

    # with open('c.json', 'r') as f:
    #     slide_articles = load(f)

    # data = {
    #     'news_categories': news_categories if email is None else user.categories.split(','),
    #     'slide_articles': slide_articles,
    #     "news_sort": news_filter,
    #     'daily_news': daily_new
    # }

    # Test Code #

    # Production Code #

    data = {
        'news_categories': news_categories if email is None else user.categories.split(','),
        'slide_articles': carousel_news(','.join(news_sources_id), ','.join(news_sources_url)) if email is None else carousel_news(','.join(news_id), ','.join(news_url)),
        "news_sort": news_filter,
        'daily_news': daily_news(news_categories, ','.join(news_sources_id), ','.join(news_sources_url) , email) if email is None else daily_news(user.categories.split(','), ','.join(news_id), ','.join(news_url) ,email)
    }

    # Production Code #

    try:

        news_articles = NewsArticle.objects.filter(title=title)

        if news_articles.exists():


            news_likes = news_articles[0].likes.filter(user__user__email=email)

            if news_likes.exists():
                news_articles[0].likes.remove(user)
                print('exist')
                print('if', news_articles[0].likesCount())
                print('if', news_articles[0].userLiked(email))
            else:
                news_articles[0].likes.add(user)
                print('else', news_articles[0].likesCount())
                print('else', news_articles[0].userLiked(email))

        else:
            heading = [a for a in data['daily_news'][category][sort]['articles']
                       if a['title'] == title][0]

            adding_news_article = NewsArticle(
                sources=heading['source'],
                author=heading['author'],
                title=heading['title'],
                description=heading['description'],
                url=heading['url'],
                url_to_image=heading['urlToImage'],
                published_at=heading['publishedAt'],
                content=heading['content'],
            )
            adding_news_article.save()
            news_articles[0].likes.add(user)


        print(news_articles[0].likes)

    except:


        print("NO ARTICLE")

    data_json = dumps(data)

    return render(request, 'index.html', context={"data": data, "data_json": data_json})


def trending(request):
    return render(request, 'trending.html')

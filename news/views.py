from django.shortcuts import render , redirect
from json import dumps, loads
from user.options import news_categories, news_sources_id, news_sources_url, news_sources_dic, news_filter
from .news import carousel_news, daily_news, total_news_result
from user.models import Profile
from .models import NewsArticle


def home(request):

    email = request.user.email if request.user.is_authenticated else None

    if request.method == "POST":
        content = loads(request.body)

        category = content['category']
        sort = content['sort']
        title = content['title']
        btnType = content['btnType']

    try:
        user = Profile.objects.filter(user__user__email=email)[0]

        news_id = [news_sources_dic[source][0]
                   for source in user.sources.split(',')]
        news_url = [news_sources_dic[source][1]
                    for source in user.sources.split(',')]

    except:
        print("NO USER")

    data = {
        'news_categories': news_categories if email is None else user.categories.split(','),
        'slide_articles': carousel_news(','.join(news_sources_id), ','.join(news_sources_url)) if email is None else carousel_news(','.join(news_id), ','.join(news_url)),
        "news_sort": news_filter,
        'daily_news': daily_news(news_categories, ','.join(news_sources_id), ','.join(news_sources_url), email) if email is None else daily_news(user.categories.split(','), ','.join(news_id), ','.join(news_url), email)
    }

    try:

        if request.user.is_authenticated:

            news_articles = NewsArticle.objects.filter(title=title)

            if news_articles.exists():

                news_likes = news_articles[0].likes.filter(
                    user__user__email=email)
                news_saved = news_articles[0].saved.filter(
                    user__user__email=email)


                if btnType == "Like":
                    news_articles[0].likes.remove(user) if news_likes.exists(
                    ) else news_articles[0].likes.add(user)

                if btnType == "Bookmark":
                    news_articles[0].saved.remove(user) if news_saved.exists(
                    ) else news_articles[0].saved.add(user)

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

                if btnType == "Like":
                    news_articles[0].likes.add(user)

                if btnType == "Bookmark":
                    news_articles[0].saved.add(user)


    except:

        print("NO ARTICLE")

    data_json = dumps(data)

    return render(request, 'index.html', context={"data": data, "data_json": data_json})


def trending(request):

    email = request.user.email if request.user.is_authenticated else None

    try:
        user = Profile.objects.filter(user__user__email=email)[0]


        news_id = [news_sources_dic[source][0]
                   for source in user.sources.split(',')]

        news_url = [news_sources_dic[source][1]
                    for source in user.sources.split(',')]
        top_article = NewsArticle.objects.order_by('-likes')[0]
        second_article = NewsArticle.objects.order_by('-likes')[1]
        other_articles = NewsArticle.objects.order_by('-likes')[2:]
        results = total_news_result(news_categories, ','.join(
            news_sources_id), ','.join(news_sources_url)) if email is None else total_news_result(user.categories.split(','), ','.join(news_id), ','.join(news_url))

        data = {
            "top_article": top_article,
            "second_article": second_article,
            "other_articles": other_articles,
            'news_categories': results,
        }

        return render(request, 'trending.html', context=data)
    except:
        return redirect("/")



from django.shortcuts import redirect, render
from .models import Profile
from allauth.socialaccount.models import SocialAccount
from pycountry import countries
from .options import news_categories, news_sources
from news.models import NewsArticle
from forum.models import Community_Forums


def new_user(request):

    try:
        user = Profile.objects.filter(user__user__email=request.user.email)
        if user.exists():
            return redirect('/')
        else:

            all_countries_names = list(countries)

            if request.method == "POST":

                user_account = SocialAccount.objects.get(
                    user__email=request.user.email)
                user_profile = Profile(user=user_account, DOB=request.POST.get('DOB'), country=request.POST.get(
                    'country'), categories=request.POST.get('categories'), sources=request.POST.get('sources'))
                user_profile.save()
                return redirect('/')

            data = {
                "all_countries_names": all_countries_names,
                'news_categories': news_categories,
                'news_sources': news_sources
            }

    except:
        return redirect("/")

    return render(request, 'new.html', context=data)


def user_profile(request):

    try:
        user = Profile.objects.filter(user__user__email=request.user.email)
        if user.exists():


            if request.method == "POST":
                user.update(categories=request.POST.get('categories'), sources=request.POST.get('sources'))


            bookmark_article = [article for article in NewsArticle.objects.all() if article.userActivity(request.user.email)[1] == 1]

            user_category = {category.capitalize(): category.capitalize() in user[0].categories.split(",") for category in news_categories}
            user_sources = {sources: sources in user[0].sources.split(",") for sources in news_sources}

            data = {
                "user_pic": user[0].user.extra_data['picture'],
                "user_country": user[0].country,
                "user_name": user[0].user.extra_data['name'],
                "news_sources": user_sources,
                "news_categories": user_category,
                "user_categories": user[0].categories,
                "user_sources": user[0].sources,
                "user_likes": sum(article.userActivity(request.user.email)[0] for article in NewsArticle.objects.all()),
                "user_bookmark": sum(article.userActivity(request.user.email)[1] for article in NewsArticle.objects.all()),
                "user_bookmark_articles" : bookmark_article,
                "user_forums" : Community_Forums.objects.filter(creator_email=request.user.email).count()
            }

        else:
            return redirect('/')


    except:
        return redirect("/")

    return render(request, 'profile.html', context=data)

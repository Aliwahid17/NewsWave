from django.shortcuts import redirect, render, get_object_or_404
from .models import Profile
from allauth.socialaccount.models import SocialAccount
from pycountry import countries

# Create your views here.


def new_user(request):
    # print(request.user)
    # print(request.user , request.method , request.user.is_authenticated)
    # print(request.user , request.method , request.user.is_authenticated , request.user.email)
    # user = Profile.objects.get(user__user__email=request.user.email)
    # print(user == '')

    # if request.user == "AnonymousUser" or  not user == '':
    #     return redirect('/')

    # if()

    # v = Profile.objects.filter(user__user=request.user)

    # print(v)

    # Profile.user = request.user
    # Profile.categories = ['fdf','sfs']
    # Profile.sources = ['sfs','dfsf']
    # Profile.save()
    # b = SocialAccount.objects.get(user__email=request.user.email)
    # # print(b.last_login)
    # v = Profile(user=b,categories=['fs','fs'],sources=['df','fd'])
    # v.save()

    # if request.method == "POST"  and  request.user == "AnonymousUser":
    #     return redirect('/')
    # print(request.user)

    # try:
    #     user = Profile.objects.get(user=request.user)
    #     if request.user == "AnonymousUser" or  not user == '':
    #         return redirect('/')
    # except:
    #     return redirect('/')
    # print(Profile.objects.get(user__user__email=request.user.email))
    # print(Profile.objects.get(user__user__username=request.user))
    # print(request.get)

    # print(Profile.objects.)

    # print(Profile.objects.filter(user__user__email=request.user.email).exists())
    # print(Profile.objects.filter(user__user__email=request.user.email))
    # print(get_object_or_404(Profile,user__user__email=request.user.email ))

    news_categories = [
        "Business",
        "Entertainment",
        "General",
        "Health",
        "Science",
        "Sports",
        "Technology",
        "Automotive",
        "Politics",
        "Education",
        "Environment",
        "Food",
        "Gaming",
        "Music",
        "Real Estate",
        "Travel",
        "Style",
        "Books",
        "Art",
        "Film",
    ]

    news_sources = [
        "Associated Press",
        "BBC News",
        "CNN",
        "Reuters",
        "The New York Times",
        "The Washington Post",
        "Fox News",
        "Al Jazeera English",
        "The Guardian",
        "The Times of India",
        "ESPN",
        "Business Insider",
        "Bloomberg",
        "TechCrunch",
        "National Geographic",
        "IGN",
        "The Verge",
        "MTV News",
        "USA Today",
        "CBS News",
    ]

    try:
        user = Profile.objects.filter(user__user__email=request.user.email)
        if user.exists():
            return redirect('/')
        else:

            print('hello')

            all_countries_names = list(countries)

            if request.method == "POST":

                # print(
                #     request.POST.get('DOB'),
                #     request.POST.get('categories'),
                #     request.POST.get('sources'),
                # )

                user_account = SocialAccount.objects.get(user__email=request.user.email)
                user_profile = Profile(user=user_account, DOB=request.POST.get('DOB'),country=request.POST.get('country'),categories=request.POST.get('categories'), sources=request.POST.get('sources'))
                user_profile.save()
                return redirect('/')

                # print(
                #     request.POST.get('DOB'),
                #     )

            data = {
                "all_countries_names": all_countries_names,
                'news_categories': news_categories,
                'news_sources' : news_sources
            }

    except:
        return redirect("/")

    return render(request, 'new.html', {'data': data})

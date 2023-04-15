from django.shortcuts import render, redirect
from user.options import news_sources_dic, news_categories
from user.models import Profile
from .models import CommunityForums
from json import dumps


# Create your views here.

def forum_home(request):

    email = request.user.email if request.user.is_authenticated else None

    try:
        user = Profile.objects.filter(user__user__email=email)[0]

    except:
        print("NO USER")

    # print(CommunityForums.objects.all())

    forum_tags = [[x , x.tags] for x in CommunityForums.objects.order_by('-votes')]

    forum_categories = news_categories if email is None else user.categories.split(",")
    
    
    # all_forum = {}



    # for category in user.categories.split(","):
    #     for tags in forum_tags:
    #         if category in tags[1]:
    #             all_forum.setdefault(category, []).append(tags[0])

    # all_forum = {category: [tags[0] for tags in CommunityForums.objects.all(
    # ) if category in tags[1]] for category in user.categories.split(",")}


    all_forum = {category.title() : [tags[0] for tags in forum_tags if category.title() in tags[1] ] for category in forum_categories  }


    data = {
        "forum_categories": news_categories if email is None else user.categories.split(','),
        "all_forum" : all_forum
    }

    data_json = dumps(forum_categories)

    return render(request, "forum/index.html",context={"data": data, "data_json": data_json})


def create_forum(request):

    try:
        user = Profile.objects.filter(user__user__email=request.user.email)
        if user.exists():
            if request.method == "POST":

                forum_post = CommunityForums(
                    title=request.POST.get("title"),
                    description=request.POST.get("description"),
                    tags=request.POST.get('categories'),
                    votes=0,
                    creator_name=user[0].user.extra_data['name'],
                    creator_image=user[0].user.extra_data['picture'],
                )

                forum_post.save()

                return redirect("/forum/")

            data = {
                'news_categories': news_categories,
            }

        else:
            return redirect('/')

    except:
        return redirect("/")

    return render(request, "forum/create.html", context=data)

from django.shortcuts import render, redirect
from user.options import news_sources_dic, news_categories
from user.models import Profile
from .models import Community_Forums, Forums_Votes , Comments
from json import dumps, loads
from django.dispatch import Signal

# Create your views here.

def forum_home(request):

    email = request.user.email if request.user.is_authenticated else None

    if request.method == "POST":
        content = loads(request.body)

        title = content['title']
        votes = content['votes']
        voteCategory = content['voteCategory']

        print(content['title'], content['votes'], content['voteCategory'])

    # Vote_Category.objects.all().delete()
    # print(Vote_Category.objects.all())
    try:
        user = Profile.objects.filter(user__user__email=email)[0]
        community_forum = Community_Forums.objects.filter(title=title)
        forum_vote = Forums_Votes.objects.filter(user=user , forum=community_forum[0])

        user_votes = community_forum[0].user_votes.filter(user__user__email=email)


        if len(forum_vote) == 0:
            Forums_Votes(
                user=user,
                forum=community_forum[0],
                vote=voteCategory
            ).save()
        else:
            forum_vote.update(vote=voteCategory)


        # community_forum[0].votes = votes
        community_forum.update(votes=votes)
        community_forum.user_votes.remove(user) if user_votes.exists() else community_forum.user_votes.add(user)


        # delete_community_forum(Community_Forums,community_forum[0].title, "dfdf")

        # community_forum_trigger = Signal(providing_args=['titles'])
        # community_forum_trigger.send(
        #     sender=Community_Forums)

        # community_forum_trigger = Signal(providing_args=['titles'])
        # titles = ['Title 1', 'Title 2', 'Title 3']
        # community_forum_trigger.send(sender=Community_Forums, titles=titles)


        # print(Community_Forums.de)


        # community_forum.user_votes.remove(user) if 

                    #        news_articles[0].likes.remove(user) if news_likes.exists(
                    # ) else news_articles[0].likes.add(user)

    except:
        print("NO USER")

    # print(CommunityForums.objects.all())

    forum_tags = [[x, x.tags]
                  for x in Community_Forums.objects.order_by('-votes')]

    forum_categories = news_categories if email is None else user.categories.split(
        ",")

    # all_forum = {}

    # for category in user.categories.split(","):
    #     for tags in forum_tags:
    #         if category in tags[1]:
    #             all_forum.setdefault(category, []).append(tags[0])

    # all_forum = {category: [tags[0] for tags in CommunityForums.objects.all(
    # ) if category in tags[1]] for category in user.categories.split(",")}

    all_forum = {category.title(): [tags[0] for tags in forum_tags if category.title(
    ) in tags[1]] for category in forum_categories}

    for key, value in all_forum.items():
        try:
            value[0].meter = Forums_Votes.objects.get(
                user=user, forum=value[0]).vote
        except:
            if len(value) != 0:
                value[0].meter = "No" 


    # for key , value in all_forum.items():
    #     # print(value[0])
    #     value[0] if len(value) != 0 else print(value)

    # print(Community_Forums.)

    data = {
        "forum_categories": news_categories if email is None else user.categories.split(','),
        "all_forum": all_forum
    }

    data_json = dumps(forum_categories)

    return render(request, "forum/index.html", context={"data": data, "data_json": data_json})


def create_forum(request):

    try:
        user = Profile.objects.filter(user__user__email=request.user.email)
        if user.exists():
            if request.method == "POST":

                forum_post = Community_Forums(
                    title=request.POST.get("title"),
                    description=request.POST.get("description"),
                    tags=request.POST.get('categories'),
                    votes=0,
                    creator_email=user[0].user.extra_data['email'],
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




def forum_view(request , uuid):

    try:
        user = Profile.objects.filter(user__user__email=request.user.email)[0]
        forum = Community_Forums.objects.get(uuid=uuid)
        total_comments_count = Comments.objects.count()
        total_comments = Comments.objects.order_by("-published_at")


        if request.method == "POST":
            Comments(
                post=forum,
                user=user,
                comment=request.POST.get('comment')
            ).save()

        data = {
            "forum":forum,
            "total_comments" : total_comments,
            "total_comments_count" : total_comments_count,
        }

    except:

        return redirect("/")

    return render(request , "forum/view.html" , context=data)
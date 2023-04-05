from allauth.socialaccount.models import SocialAccount


def user_details(request):

    try:
        if request.user.is_authenticated:
            user = SocialAccount.objects.get(user__email=request.user.email)
            return {
                "user_picture": user.extra_data['picture'],
            }
        else:
            return {}
    except:
        return {}

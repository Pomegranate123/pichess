from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import  User
from django.core.cache import cache
from .conf import online_status_settings as config


# Create your views here.

def profile(request):
    username = request.user
    try:
        rating = Users.objects.filter(username=username).values("rating")
        certain = True
        data = {
            #'username': username,
            'rating': rating
        }
    except:
        rating = "1500"
        certain = False
        data = {
            #'username': username,
            'rating': str(rating) + "?"     
        }

    return JsonResponse(data)

def players(request):

    online_users = cache.get(config.CACHE_USERS)
    print(online_users)
    return JsonResponse(
        online_users, safe=False
    )
    # return render(request, 'home/list.html', )

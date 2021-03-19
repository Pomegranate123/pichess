from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import  User
from django.core.cache import cache


# Create your views here.

def profile(request):
    username = request.user
    try:
        rating = User.objects.filter(username=username).values("email")[0]['email']
        certain = True
        data = {
            #'username': username,
            'rating': rating,
            'online': request.user.online_check()
        }
        return JsonResponse(data)
    except:
        rating = "1500"
        certain = False
        data = {
            #'username': username,
            'rating': str(rating) + "?",
            'online': request.user.online_check()
        }
        return JsonResponse(data)

def players(request):
    all_users = User.objects.all()
    online_players = []
    for user in all_users:
        if user.online_check():
            online_players.append(user.username)

    online_list = {'online_players': online_players}

    return JsonResponse(online_list)
    
    # return render(request, 'home/list.html', )

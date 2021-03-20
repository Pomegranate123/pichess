from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import  User
from django.core.cache import cache
from channels_presence.models import Room
import json


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
    users = list(Room.get_users(1).values())
    online_list = []
    for i, user in enumerate(users):
        online_list.append(users[i]["username"])

    data = {
        'online': online_list
    }
    return JsonResponse(data)

    """
     users = room.get_users() 
     data = {
        'online_players': online_players
     }
     return JsonResponse(data)
     """

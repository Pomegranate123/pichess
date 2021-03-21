from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'game/index.html', {})

def room(request, room_name):
    return render(request, 'game/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def rating(request):
    opponent_rating = int(request.GET.get('rating').split("?")[0])
    win = request.GET.get('win')
    user_rating = int(request.user.email)
    if win:
        added_rating = round((opponent_rating - user_rating) * 0.04) + 10
    else:
        added_rating = -(round((opponent_rating - user_rating) * 0.04) + 10)
    if added_rating < 1:
        added_rating = 1
    new_rating = user_rating + added_rating
    user = User.objects.get(username=request.user)
    user.email = new_rating
    user.save()
    data = {
        'rating': new_rating
    }

    return JsonResponse(data)
   


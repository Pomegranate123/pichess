from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse


def index(request):
    return render(request, 'game/index.html', {})

def room(request, room_name):
    return render(request, 'game/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def rating(request, opponent, win):
    opponent_rating = opponent['rating']
    user_rating = request.user.player.rating
    if win:
        added_rating = round((opponent_rating - user_rating) * 0.04) + 10
    else:
        added_rating = -(round((opponent_rating - user_rating) * 0.04) + 10)
    if added_rating < 1:
        added_rating = 1
    new_rating = user_rating + added_rating
    p = Player(id=request.user.id, rating=new_rating)
    p.save()
    data = {
        'rating': new_rating
    }

    return JsonResponse(data)
   


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Player
from .forms import PlayerForm
import json
# Create your views here.


def log_in(request):
    received_json = json.loads(request.body)
    username = received_json['username']
    password = received_json['password']
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        print("logged in")
        login(request, user)
        return HttpResponse(status=200) # OK
    return HttpResponse("Invalid username or password", status=400) # Bad Request

def log_out(request):
    logout(request)
    return HttpResponse(status=200)

def profile(request):
    if request.user.is_authenticated:
        USERNAME = request.user.username
        RATING = request.user.email

        """
        if request.user.player.rating != NULL:
            RATING = request.user.player.rating
        else:
            p = Player(id=request.user.id, rating=1500)
            p.save()
        """

        context = {
            'username': USERNAME,
            'rating': RATING
        }
        return JsonResponse(context)
    else:
        return HttpResponse("User not logged in", status=400)

def register(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        username = received_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            return HttpResponse("User exists", status=400)
        
        # check username in database
        user = User.objects.create_user(
            received_data['username'],
            '1500',
            received_data['password']
        )

        return HttpResponse(status=200)


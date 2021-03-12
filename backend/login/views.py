from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Player
from .forms import PlayerForm
# Create your views here.


def log_in(request):
    received_json = json.loads(request.body)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('../profile')
    else:
        return redirect('../../login')

def profile(request):
    if User.is_authenticated:
        USERNAME = request.user.username
        RATING = request.user.player.rating

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
        return HttpResponse("LOGIN!")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        player_form = PlayerForm()

        if form.is_valid():
            user = form.save()
            player = player_form.save(commit=False)
            player.user = user
            player.save()
            return redirect('../../login/')

    else:
        form = UserCreationForm()
        player_form = PlayerForm()


    context = {
        'form': form,
        'player_form': player_form
    }
    return render(request, 'login/register.html', context)



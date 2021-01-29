from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Player
# Create your views here.

def test(request):
    return render(request, "login/form.html")

def register(request):
    if request.method == 'POST':
        form = request.User

        #if form.is_valid():
        USERNAME = form.get('username')
        PASSWORD = form.get('password')
        user = Player.objects.create(
            username = USERNAME,
            password = PASSWORD,
            rating = 1500
        )
        messages.succes(request, f'Account created for {username}')

    else:
        #form = formid()
        pass
    
    context = {
        'username': request.user
    }

    return render(request, 'login/regist.html', context)




   
    

"""
def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)

        user = authenticate(username=form.get('username'), password=form.get('password'))
                
        if user is not None:
            login(request, user)
        else:
#            pass
"""
#    return render(request, "login/form.html")

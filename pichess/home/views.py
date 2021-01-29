from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import  User

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



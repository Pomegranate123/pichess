from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile),
    path('players', views.players),
    path('get_rating', views.get_rating)
]

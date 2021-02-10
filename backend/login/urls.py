from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('profile/', views.profile),
    path('register/', views.register),
    path('authenticate/', views.log_in)
]


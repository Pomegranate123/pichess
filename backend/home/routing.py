from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path('lobby/', consumers.LobbyConsumer.as_asgi())
]

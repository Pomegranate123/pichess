import os
from channels.layers import get_channel_layer
from django.urls import re_path, path
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import game.consumers as game_consumers
import home.consumers as home_consumers

channel_layer = get_channel_layer()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pichess.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  'websocket': AuthMiddlewareStack (
        URLRouter([
            re_path('ws/game/(?P<room_name>\w+)/$', game_consumers.GameConsumer.as_asgi()),
            re_path('ws/lobby', home_consumers.LobbyConsumer.as_asgi())
        ])
    ),
})

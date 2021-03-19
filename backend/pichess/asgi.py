import os
from django.conf.urls import url
from django.core.asgi import get_asgi_application
from django.urls import re_path, path


import game.consumers as game_consumers
import home.consumers as home_consumers
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.layers import get_channel_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pichess.settings')

channel_layer = get_channel_layer()

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  'websocket': AuthMiddlewareStack (
        URLRouter([
            re_path('wss/game/(?P<room_name>\w+)/$', game_consumers.GameConsumer.as_asgi()),
            #re_path('wss/lobby', home_consumers.LobbyConsumer.as_asgi())
        ])
    ),
})

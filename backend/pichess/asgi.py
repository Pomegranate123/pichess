import os
from django.conf.urls import url
from django.core.asgi import get_asgi_application
from django.urls import re_path, path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pichess.settings')
django_asgi_app = get_asgi_application()

import game.consumers as game_consumers
import home.consumers as home_consumers
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  'websocket': AuthMiddlewareStack (
        URLRouter([
            re_path('ws/game/(?P<room_name>\w+)/$', game_consumers.GameConsumer.as_asgi()),
            re_path('ws/lobby', home_consumers.LobbyConsumer.as_asgi())
        ])
    ),
})

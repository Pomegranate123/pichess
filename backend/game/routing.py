from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    # path('ws/game//', consumers.GameConsumer.as_asgi()),
    re_path(r'ws/game/(?P<room_name>\w+)/$', consumers.GameConsumer.as_asgi())
]

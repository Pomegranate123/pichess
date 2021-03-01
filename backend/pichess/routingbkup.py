"""
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
import game.routing
from game.consumers import GameConsumer


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                game.routing.websocket_urlpatterns
            ]
        )
    ),
})"""

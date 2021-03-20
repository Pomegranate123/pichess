import json
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from channels_presence.models import Presence
from channels_presence.models import Room

class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        super().connect()
        Room.objects.add("online", self.channel_name, self.scope["user"])

    def receive(self, close_code):
        presence.objects.touch(self.channel_name) 

    def disconnect(self, close_code):
        Room.objects.remove("online", self.channel_name)
        

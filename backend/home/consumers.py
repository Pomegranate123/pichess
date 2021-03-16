import asyncio
import json
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

class LobbyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        channel_layer = get_channel_layer()
        print("connected", event)
        await self.send({
            'type': 'websocket.accept'
        })
        
        await self.channel_layer.group_add(
            'lobby',
            self.channel_name
        )        
        
        #self.accept()

    async def websocket_receive(self, event):
        print(event['text'])
        #event_json = json.loads(event['text'])
        
    async def websocket_disconnect(self, event):
        pass


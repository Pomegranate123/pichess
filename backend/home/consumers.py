import asyncio
import json
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.exceptions import StopConsumer
from datetime import timedelta

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
        print(event)
        print(event['text'])
        print(json.loads(event['text']))
        #event_json = json.loads(event['text'])
        await self.send({
            'event': 'message',
            'type': 'websocket.send',
            'text': event['text'],
        })

        
    async def websocket_disconnect(self, event):
        print("Disconnected", event)
        raise StopConsumer

import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

class LobbyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            'type': 'websocket.accept'
        })
        
        await self.channel_layer.group_add(
            'lobby',
            self.channel_name
        )        
        
        await self.channel_layer.group_send(
            'lobby',
            {
                'list': channel_layer.group_channels('lobby')
            }
        )

        self.accept()

    async def websocket_receive(self, event):
        event_json = json.loads(event)
        
        await self.online_player_query()

        await self.channel_layer.group_send(
            'lobby',
            {
                'list': channel_layer.group_channels('lobby')
            }
        )

    async def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discord)(
            'lobby',
            self.channel_name
        )


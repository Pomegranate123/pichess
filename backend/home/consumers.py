import json
import asyncio
from channels.exceptions import StopConsumer
from channels.consumer import AsyncConsumer
from channels_presence.models import Presence
from channels_presence.models import Room
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async





class LobbyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await database_sync_to_async(Room.objects.add)("online", self.channel_name, self.scope["user"])
        await self.channel_layer.group_add(
            "online",
            self.channel_name
        )
        
              
        await self.channel_layer.group_send(
            "online",
            {
                "type": "send_update",
                "text": "update"
            }
        )
    

        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        await database_sync_to_async(presence.objects.touch)(self.channel_name)
        """
        await self.channel_layer.group_send(
            "online",
            {
                "type": "send_challenge",
                "text": event
            })
        """
        pass

    async def send_challenge(self, event):
        self.send({
            "type": "websocket.send",
            "text": event
        })

    async def send_update(self, event):
        self.send({
            "type": "websocket.send",
            "text": event
        })

    async def websocket_disconnect(self, event):
        print("DISCONNECTED", event)
        await database_sync_to_async(Room.objects.remove)("online", self.channel_name)

        await self.channel_layer.group_send(
            "online",
            {
                "type": "send_update",
                "text": "update"
            }
        )
        
    
        await self.channel_layer.group_discard(
            "online",
            self.channel_name
        )
        




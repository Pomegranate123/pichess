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
        print(f"Added to online group: {self.channel_name}")
              
        await self.send({
            "type": "websocket.accept"
        })

        await self.channel_layer.group_send(
            "online",
            {
                "type": "send_update",
                "text": "update"
            })

    async def websocket_receive(self, event):
        msg = json.loads(event["text"])
        if msg["type"] == "add":
            await database_sync_to_async(Room.objects.add)("online", self.channel_name, self.scope["user"])
            await self.channel_layer.group_send(
                "online",
                {
                    "type": "send_update",
                    "text": "update"
                })

        if msg["type"] == "remove":
            await database_sync_to_async(Room.objects.remove)("online", self.channel_name)
            await self.channel_layer.group_send(
                "online",
                {
                    "type": "send_update",
                    "text": "update"
                })

        if msg["type"] == "challenge":
            await self.channel_layer.group_send(
                "online",
                {
                    "type": "send_challenge",
                    "text": event["text"]
                })

    async def send_challenge(self, event):
        await self.send({
            "event": "message",
            "type": "websocket.send",
            "text": event["text"]
        })

    async def send_update(self, event):
        await self.send({
            "event": "message",
            "type": "websocket.send",
            "text": '{"type":"update"}'
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
        




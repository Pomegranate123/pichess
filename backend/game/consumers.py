import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

class GameConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        
        # [white player name][black player name]
        self.white_player = self.scope['url_route']['kwargs']['white_player']  
        self.black_player = self.scope['url_route']['kwargs']['black_player'] 
        self.room_group_name = self.white_player + self.black_player
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        event_json = json.loads(event['text'])
        print(event_json)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                    'type': 'make_move',
                    'text': event['text']
            })
        
         

    async def make_move(self, event):
        await self.send({
            "event": "message",
            "type": "websocket.send",
            "text": event['text']
        })
    


    async def websocket_disconnect(self, event):
        print("disconnected", event)
        
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        
        # [white player name][black player name]
        self.white_player = self.scope['url_route']['kwargs']['white_player']  
        self.black_player = self.scope['url_route']['kwargs']['black_player'] 
        self.room_group_name = self.white_player + self.black_player
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept",
        })



    async def websocket_receive(self, event):
        event_json = json.loads(event['text'])

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                    'type': 'send_message',
                    'text': event['text']
            })

    async def send_message(self, event):
        await self.send({
            "event": "message",
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect():
        print("disconnected", event)
        
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )




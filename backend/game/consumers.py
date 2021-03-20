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
        print(self.room_group_name)
        print("Channel name: " + str(self.channel_name))
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept",
        })

        """
        board_obj = await self.get_board(me, opponent)
        game_room = "UNIQUE_NAME"
        self.game_room = game_room
        await self.channel_layer.group_add(
            game_room,
            self.channel_name
        )
        
        await self.send({
            "type": "websocket.send",
        })
        """

    async def websocket_receive(self, event):
        event_json = json.loads(event['text'])
        print(event_json)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                    'type': 'make_move',
                    'text': event['text']
            }
        )
        
        """
        front_move = event.get('action', None)
        if move is not None:
            loaded_move = json.loads(front_move)
            move = loaded_move.get('move')
            new_event = {
                "type": "make_move",
                "action": move
            }
            await self.channel_layer.group_send(
                self.game_room,
                new_event
            )
        """ 

    async def make_move(self, event):
        print("making move")
        await self.send({
            "event": "message",
            "type": "websocket.send",
            "text": event['text']
        })
        print(event['text'])


    async def websocket_disconnect(self, event):
        print("disconnected", event)
        """
         async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        """
        

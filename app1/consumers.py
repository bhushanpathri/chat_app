from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from .models import *
class NewConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.room_obj = Room.objects.get(room_name=self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({'message': 'You are connected to Django'}))

    def receive(self, text_data):
        # re= json.dump(text_data)
        # print(type(re))
        reply=json.loads(text_data)
        print(type(reply))
        print("*************",reply)
        chats_detail = Chats.objects.create(room=self.room_obj,text_message=reply["message"],sender=reply["sender"])
        print(chats_detail)
        chats_detail.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'send_message',
                'payload': text_data
            }
        )

        # self.send(text_data = json.dumps({'answer' : text_data }))

    def disconnect(self, *args, **kwargs):
        print('Disconnected')

    def send_message(self, event):
        data = event['payload']
        data = json.loads(data)
        print(data)
        self.send(text_data=json.dumps({'answer': data}))
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    current_online = models.ManyToManyField(User)


class Chats(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room")
    text_message = models.TextField(blank=True, null=True)
    # sender = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="user")
    sender = models.CharField(max_length=64)
    message_read = models.BooleanField(default=False)



from django.db import models

# Create your models here.

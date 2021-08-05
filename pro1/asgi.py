"""
ASGI config for pro1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os


from django.core.asgi import get_asgi_application


from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app1.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')


application = get_asgi_application()

ws_patterns = [

    path('ws/<room_name>/', NewConsumer)

]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
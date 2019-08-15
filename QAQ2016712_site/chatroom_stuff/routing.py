from django.urls import path
from chatroom_stuff import consumers


websocket_urlpatterns = [
    path('ws/chat-room-select/<str:room_name>/$', consumers.chatconsumer),
]
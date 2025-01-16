# your_app/urls.py
from django.urls import path
from . import views
app_name='chatting'
urlpatterns = [
    path('<str:room_name>/<str:otheruser>', views.chat_room, name='chat_room'),
]

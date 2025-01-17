# your_app/urls.py
from django.urls import path
from . import views
app_name='chatting'
urlpatterns = [
    path('<str:origin_user_id>/<str:otheruser_id>', views.create_room, name='create_room'),
    path('<str:room_name>/<str:origin_user_id>/<str:otheruser_id>', views.chat_room, name='chat_room'),
]

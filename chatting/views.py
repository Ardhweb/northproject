from django.shortcuts import render
# Create your views here.
# your_app/views.py
from django.shortcuts import render,redirect
from .models import ChatThread,  ChatText
import uuid
import shortuuid
from django.contrib.auth.models import User
from django.urls import reverse

def create_room(request, origin_user_id, otheruser_id):
    get_origin = User.objects.get(id=origin_user_id)
    get_other = User.objects.get(id=otheruser_id)
    room_uuid =  shortuuid.uuid()
    room_name = f"room_{room_uuid}{origin_user_id}{otheruser_id}"
    room, created = ChatThread.objects.get_or_create(room_name=room_name,origin_user=get_origin,other_user=get_other)
    url = reverse('chatting:chat_room', kwargs={'room_name': room_name, 'origin_user_id':origin_user_id,'otheruser_id':otheruser_id})
    return redirect(url)

def chat_room(request, room_name, origin_user_id, otheruser_id):
    return render(request, 'chat.html', {
        'room_name': room_name,
        #'otheruser':otheruser
    })

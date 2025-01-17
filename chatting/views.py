from django.shortcuts import render
# Create your views here.
# your_app/views.py
from django.shortcuts import render,redirect
from .models import ChatThread,  ChatText
import uuid
import shortuuid
from django.contrib.auth.models import User
from django.urls import reverse
#single person chat
from django.shortcuts import redirect
from django.urls import reverse
from django.db import IntegrityError
from django.db.models import Q

def create_room(request, origin_user_id, otheruser_id):
    try:
        # Generate a unique room name
        room_uuid = shortuuid.uuid()
        room_name = f"room_{room_uuid}{origin_user_id}{otheruser_id}"
        
        # Attempt to create a new ChatThread
        room = ChatThread.objects.create(
            room_name=room_name,
            origin_user=origin_user_id,
            other_user=otheruser_id
        )
    except IntegrityError:
        # Handle the case where the unique constraint is violated
        room = ChatThread.objects.filter(
            Q(origin_user=origin_user_id, other_user=otheruser_id) |
            Q(origin_user=otheruser_id, other_user=origin_user_id)
        ).filter(active=True).first()
        
        if room:
            # If an active room exists, redirect to it
            room_name = room.room_name
        else:
            # If no active room exists, activate an existing one
            room = ChatThread.objects.filter(
                Q(origin_user=origin_user_id, other_user=otheruser_id) |
                Q(origin_user=otheruser_id, other_user=origin_user_id)
            ).first()
            room.active = True
            room.save()
            room_name = room.room_name

    # Redirect to the appropriate chat room
    url = reverse('chatting:chat_room', kwargs={
        'room_name': room_name,
        'origin_user_id': origin_user_id,
        'otheruser_id': otheruser_id
    })
    return redirect(url)



def chat_room(request, room_name, origin_user_id, otheruser_id):
    return render(request, 'chat.html', {
        'room_name': room_name,
        #'otheruser':otheruser
    })

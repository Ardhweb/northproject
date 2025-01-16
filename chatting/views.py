from django.shortcuts import render
# Create your views here.
# your_app/views.py
from django.shortcuts import render

def chat_room(request, room_name,otheruser):
    return render(request, 'chat.html', {
        'room_name': room_name,
        'otheruser':otheruser
    })

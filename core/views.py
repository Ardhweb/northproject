from django.shortcuts import render
import uuid;
# Create your views here.
from django.contrib.auth.models import User
from chatting.models import ChatThread, ChatText
from django.db.models import Q
def index(request):
    logged_user_id = request.user.id
    current_rooms = ChatThread.objects.filter(
    Q(origin_user=logged_user_id) | Q(other_user=logged_user_id))
    auth_user = User.objects.exclude(id=logged_user_id)
    testroom = uuid.uuid4().hex
    context = {
        'auth_user':auth_user,
        'testroom':testroom,
        'active_rooms':current_rooms,
    }
    return render(request, "index.html", context)


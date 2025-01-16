from django.shortcuts import render
import uuid;
# Create your views here.
from django.contrib.auth.models import User
def index(request):
    auth_user = User.objects.all()
    testroom = uuid.uuid4().hex
    context = {
        'auth_user':auth_user,
        'testroom':testroom,
    }
    return render(request, "index.html", context)


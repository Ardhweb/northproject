from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
def index(request):
    auth_user = User.objects.all()
    context = {
        'auth_user':auth_user
    }
    return render(request, "index.html", context)


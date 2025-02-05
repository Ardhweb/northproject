from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm                                       
from django.contrib import auth, messages
from .forms import LoginForm, UserRegistrationForm
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.urls import reverse
from django.contrib.auth import logout as auth_logout

def user_logout(request):
    auth_logout(request)  # Call Django's built-in logout function
    return redirect("core:index")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("core:index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user = authenticate(request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect("core:index")
    else:
        user_form = UserRegistrationForm()
    return render(request,'accounts/register.html',{'user_form': user_form})

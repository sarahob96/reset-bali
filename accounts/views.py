from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, Register
from .models import login, newUser


def account_login(request):
    
    if request.method == 'post':
        form = LoginForm()
        if form.is_valid():
            form.save()
            return redirect()

    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {"form":form})

def accountRegister(request):

    if request.method == 'post':
        form = Register()
        if form.is_valid():
            form.save()
            return redirect()

    else:
        form = Register()

    return render(request, 'accounts/registration.html', {"form":form})
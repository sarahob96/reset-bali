from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def new_account(request):
    context = {}
    return render(request, 'accounts/registration.html', context)

def login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.success(request, ("Error with logging in, please try again"))
            return redirect('login')

    context = {}
    return render(request, 'accounts/login.html', context)


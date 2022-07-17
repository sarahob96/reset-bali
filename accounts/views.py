from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, Register
from .models import login, newUser


def account_login(request):
    
    form = LoginForm()
    if request.method == 'POST':

        login_fields = {
            'userName': request.POST['userName'],
            'userPassword': request.POST['userPassword'],
        }
        form = LoginForm(login_fields)
        if form.is_valid():
            form.save()
        
        else:
            form = LoginForm()
    
    return render(request, 'accounts/login.html', {"form": form})

def accountRegister(request):

    form = Register()
    if request.method == 'POST':

        account_fields = {
            'userName': request.POST['userName'],
            'email': request.POST['email'],
            'userPassword': request.POST['userPassword'],
            'userPasswordRepeat': request.POST['userPasswordRepeat'],
        }

        form = Register(account_fields)
 
        if form.is_valid():
            form.save()
            return redirect('login')
        
        else:
            form = Register()

    return render(request, 'accounts/registration.html', {"form": form})
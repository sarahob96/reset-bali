from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

global user

def login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Error with logging in, please try again"))
            return redirect('login')

    context = {}
    return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    messages.success(request, ("You are logged out"))
    return redirect('home')

def new_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
        
    return render(request, 'accounts/registration.html', {'form': form, })

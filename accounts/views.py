from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages


def account_login(request):
    return render(request, 'accounts/accounts.html', {})
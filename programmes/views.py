from django.shortcuts import render

# Create your views here.

def locations(request):
    return render(request, 'programmes/locations.html')

def rewind(request):
    return render(request, 'programmes/rewind.html')

def restart(request):
    return render(request, 'programmes/restart.html')

def renew(request):
    return render(request, 'programmes/renew.html')

def ubud(request):
    return render(request, 'programmes/ubud.html')

def seminyak(request):
    return render(request, 'programmes/seminyak.html')   
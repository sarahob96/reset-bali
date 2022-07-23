from django.shortcuts import render
from .forms import rewind_form


# Create your views here.


def rewindbooking(request):

    form = rewind_form()     
    context = {'form': form}
    return render(request, "programmes/rewind.html", context)

def rewind(request):
    return render(request, 'programmes/rewind.html')

def locations(request):
    return render(request, 'programmes/locations.html')


def restart(request):
    return render(request, 'programmes/restart.html')

def renew(request):
    return render(request, 'programmes/renew.html')

def ubud(request):
    return render(request, 'programmes/ubud.html')

def seminyak(request):
    return render(request, 'programmes/seminyak.html')




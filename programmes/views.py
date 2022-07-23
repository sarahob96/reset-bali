from django.shortcuts import render
from .forms import rewind_form


# Create your views here.


def rewindbooking(request):

    form = rewind_form()     
    if request.method == 'POST':
        rewind_fields = {
            'name1': request.POST['name1'],
            'date': request.POST['date'],
            'programme': request.POST['programme'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
        
        }
        form = rewind_form(rewind_fields)
   
        if form.is_valid():
            form.save()
    
    return render(request, "programmes/rewind.html", {'form': form})

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




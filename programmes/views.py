from django.shortcuts import render, redirect, get_object_or_404
from .forms import rewind_form
from .models import rewind
from django.contrib.auth.models import User


# Create your views here.

def update_booking(request, booking_id):
    booking = rewind.objects.get(pk=booking_id)
    form = rewind_form(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('mybookings')

    return render(request, 'programmes/update_booking.html', {'booking': booking, 'form':form})

def rewindbooking(request):

    form = rewind_form()     
    if request.method == 'POST':
        rewind_fields = {
            'user': request.POST['user'],
            'date': request.POST['date'],
            'programme': request.POST['programme'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
        
        }
        form = rewind_form(rewind_fields)
   
        if form.is_valid():
            form.save()
   
        
    return render(request, "programmes/rewind.html", {'form': form})

def my_bookings(request):
    
    bookings = rewind.objects.filter(user=request.user)
    return render(request, 'programmes/bookings.html', {'bookings': bookings})

def rewind_page(request):
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




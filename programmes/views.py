from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from .forms import Rewind_form, Renew_form, Restart_form
from .models import Rewind, Renew, Restart


# Create your views here.


def delete_booking(request, booking_id):
    """ deletes users rewind booking """
    booking = Rewind.objects.get(pk=booking_id)
    booking.delete()
    return redirect('mybookings')


def delete_restart_booking(request, booking_id):
    """ deletes users restart booking """
    bookings_restart = Restart.objects.get(pk=booking_id)
    bookings_restart.delete()
    return redirect('mybookings')


def delete_renew_booking(request, booking_id):
    """ deletes users renew booking """
    bookings_renew = Renew.objects.get(pk=booking_id)
    bookings_renew.delete()
    return redirect('mybookings')


def update_booking(request, booking_id):
    """ updates users rewind booking """
    booking = Rewind.objects.get(pk=booking_id)
    form = Rewind_form(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('mybookings')

    return render(request, 'programmes/update_booking.html',
                  {'booking': booking, 'form': form})


def update_renew_booking(request, booking_id):
    """ updates users renew booking """
    bookings_renew = Renew.objects.get(pk=booking_id)
    form = Renew_form(request.POST or None, instance=bookings_renew)
    if form.is_valid():
        form.save()
        return redirect('mybookings')

    return render(request, 'programmes/update_booking.html',
                  {'bookings_renew': bookings_renew, 'form': form})


def update_restart_booking(request, booking_id):
    """ updates users restart booking """
    bookings_restart = Restart.objects.get(pk=booking_id)
    form = Restart_form(request.POST or None, instance=bookings_restart)
    if form.is_valid():
        form.save()
        return redirect('mybookings')

    return render(request, 'programmes/update_booking.html',
                  {'bookings_reset': bookings_restart, 'form': form})


def rewindbooking(request):
    """ user booking form for rewind """
    form = Rewind_form()
    if request.method == 'POST':
        rewind_fields = {
            'user': request.POST['user'],
            'date': request.POST['date'],
            'programme': request.POST['programme'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],

        }

        form = Rewind_form(rewind_fields)

        if form.is_valid():
            form.save()
            user = get_user(request)
            form = Rewind_form(initial={'user': user})
            return redirect(booking_confirmation)
    else:
        user = get_user(request)
        form = Rewind_form(initial={'user': user})

    return render(request, "programmes/rewind.html", {'form': form})


def renewbooking(request):
    """ user booking form for renew """
    form = Renew_form()
    if request.method == 'POST':
        renew_fields = {
            'user': request.POST['user'],
            'date': request.POST['date'],
            'programme': request.POST['programme'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],

        }

        form = Renew_form(renew_fields)

        if form.is_valid():
            form.save()
            user = get_user(request)
            form = Renew_form(initial={'user': user})
            return redirect(booking_confirmation)
    else:
        user = get_user(request)
        form = Renew_form(initial={'user': user})

    return render(request, "programmes/renew.html", {'form': form})


def restartbooking(request):
    """ user booking form for restart """
    form = Restart_form()
    if request.method == 'POST':
        restart_fields = {
            'user': request.POST['user'],
            'date': request.POST['date'],
            'programme': request.POST['programme'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],

        }

        form = Restart_form(restart_fields)

        if form.is_valid():
            form.save()
            user = get_user(request)
            form = Restart_form(initial={'user': user})
            return redirect(booking_confirmation)

    else:
        user = get_user(request)
        form = Restart_form(initial={'user': user})

    return render(request, "programmes/restart.html", {'form': form})


def my_bookings(request):
    """ filters bookings by user """
    bookings = Rewind.objects.filter(user=request.user)

    bookings_restart = Restart.objects.filter(user=request.user)

    bookings_renew = Renew.objects.filter(user=request.user)

    return render(request, 'programmes/bookings.html',
                  {'bookings': bookings, 'bookings_restart': bookings_restart,
                   'bookings_renew': bookings_renew, })


def rewind_page(request):
    """ redirects user to rewind programme page"""
    return render(request, 'programmes/rewind.html')


def locations(request):
    """ redirects user to locations page """
    return render(request, 'programmes/locations.html')


def restart(request):
    """ redirects user to restart programme page"""
    return render(request, 'programmes/restart.html')


def renew(request):
    """ redirects user to renew page """
    return render(request, 'programmes/renew.html')


def ubud(request):
    """ redirects user to ubud programmes """
    return render(request, 'programmes/ubud.html')


def seminyak(request):
    """ redirects user to seminyak programme """
    return render(request, 'programmes/seminyak.html')


def booking_confirmation(request):
    """ redirects user to booking confirmation page """
    return render(request, 'programmes/booking-confirmation.html')

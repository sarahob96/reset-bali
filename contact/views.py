from django.shortcuts import render
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import get_user

# Create your views here.


def form_contact(request):
    """
    """
   
    form = contact_form()
    if request.method == 'POST':
        contact_fields = {
           
            'name': request.POST['name'],
            'your_message': request.POST['your_message'],
            'email': request.POST['email'],
            'date': request.POST['email'],
            'phone': request.POST['phone'],
        }
        form = contact_form(contact_fields)
   
        if form.is_valid():
            form.save()
            form = contact_form()
    
    else:
        if request.user.is_authenticated:
            name = get_user(request)
            form = contact_form(initial={'name': name})

    return render(request, "contact/contact.html", {'form': form})



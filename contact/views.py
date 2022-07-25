from django.shortcuts import render
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
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

           # try: 
               ### send_mail(subject="hello", message="hello", 'admin@resetbali.com', ['sarahobrien15@gmail.com'])
           ## except BadHeaderError:
            #    return HttpResponse('invalid')
    return render(request, "contact/contact.html", {'form': form})



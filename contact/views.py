from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from .forms import contact_form


# Create your views here.


def thanks_for_contacting(request):
    """ redirects user to thank you for contacting on form submission """

    return render(request, 'contact/thanks-for-contacting.html')


def form_contact(request):
    """user contact form """

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
            return redirect('thanks_for_contacting')

    else:
        if request.user.is_authenticated:
            name = get_user(request)
            form = contact_form(initial={'name': name})

    return render(request, "contact/contact.html", {'form': form})

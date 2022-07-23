from django.shortcuts import render
from programmes.views import rewindbooking

# Create your views here.


def profiles(request):

    return render(request, 'profiles/profile.html')
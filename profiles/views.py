from django.shortcuts import render


# Create your views here.


def profiles(request):
    """ redirects user profile page """
    return render(request, 'profiles/profile.html')

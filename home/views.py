from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm 
from .models import Review
from django.views.generic import DeleteView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user

# Create your views here.

def homepage(request):

    return render(request, 'home_page/index.html')


def form_review(request):
    """
    """

    form = ReviewForm()
   
    if request.method == 'POST':
        review_fields = {
            
            'name': request.POST['name'],
            'rating': request.POST['rating'],
            'programme_attended': request.POST['programme_attended'],
            'your_experience': request.POST['your_experience'],
        }
        form = ReviewForm(review_fields)
   
        if form.is_valid():
            form.save()
            form=ReviewForm()
            
    else: 
        name = get_user(request)
        form = ReviewForm(initial={'name': name})
       
            

    reviews = Review.objects.all()
    return render(request, "home_page/index.html", {'reviews': reviews, 'form': form})


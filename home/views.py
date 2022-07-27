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

def delete_review(request, review_id):
    all_reviews = Review.objects.get(pk=review_id)
    all_reviews.delete()
    return redirect('myreviews')

def update_review(request, review_id):
    all_reviews = Review.objects.get(pk=review_id)
    form = ReviewForm(request.POST or None, instance=all_reviews)
    if form.is_valid():
        form.save()
        return redirect('myreviews')

    return render(request, 'programmes/update_booking.html', {'booking': booking, 'form':form})

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
            name = get_user(request)
            form = ReviewForm(initial={'name': name})
            
    else: 
        name = get_user(request)
        form = ReviewForm(initial={'name': name})
       
    reviews = Review.objects.all()
    return render(request, "home_page/index.html", {'reviews': reviews, 'form': form})


def my_reviews(request):
    
    all_reviews = Review.objects.filter(name=request.user)
    return render(request, 'home_page/myreviews.html', {'all_reviews': all_reviews})
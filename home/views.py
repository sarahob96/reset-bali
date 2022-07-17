from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm 
from .models import Review
from django.contrib import messages 


# Create your views here.


def form_review(request):
    """
    """
    form = ReviewForm()
    if request.method == 'POST':
        review_fields = {
            'title': request.POST['title'],
            'name': request.POST['name'],
            'rating': request.POST['rating'],
            'programme_attended': request.POST['programme_attended'],
            'your_experience': request.POST['your_experience'],
        }
        form = ReviewForm(review_fields)
    
        if form.is_valid():
           form.save()

    context = {'form': form}
    return render(request, 'home_page/index.html', context)


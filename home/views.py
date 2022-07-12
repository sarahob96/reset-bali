from django.shortcuts import render
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
            'rating': request.POST['rating'],}
        form = ReviewForm(review_fields)
        
    
        if form.is_valid():
            review = form.save()
            review.save()
                
            messages.success(request, "thanks for your review")
    else:
        messages.error(request, 'your review did not submit')

    context = {'form': form}
    return render(request, 'home_page/index.html', context)

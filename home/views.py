from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth import get_user

# Create your views here.


def homepage(request):
    """ redirects user to home page """
    return render(request, 'home_page/index.html')


def delete_review(request, review_id):
    """ deletes user review """
    all_reviews = Review.objects.get(pk=review_id)
    all_reviews.delete()
    return redirect('myreviews')


def update_review(request, review_id):
    """ updates the users review """
    all_reviews = Review.objects.get(pk=review_id)
    form = ReviewForm(request.POST or None, instance=all_reviews)
    if form.is_valid():
        form.save()
        return redirect('myreviews')

    return render(request, 'home_page/update_review.html',
                  {'all_reviews': all_reviews, 'form': form})


def form_review(request):
    """
    form view that saves review left by user
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
    return render(request, "home_page/index.html", {'reviews': reviews,
                                                    'form': form})


def my_reviews(request):
    """ filters reviews left by logged in user """
    all_reviews = Review.objects.filter(name=request.user)
    return render(request, 'home_page/myreviews.html',
                  {'all_reviews': all_reviews})

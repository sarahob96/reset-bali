from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.

def get_home_page(request):
    form = ReviewForm()
    if request.method == 'POST':
        print(request.POST)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'home_page/index.html', context)

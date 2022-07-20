from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Review
        fields = ['title', 'name', 'programme_attended', 'your_experience', 'rating']
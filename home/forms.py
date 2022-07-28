from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    review form for user review model
    """
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

    class Meta:
        model = Review
        fields = ['name', 'programme_attended', 'your_experience', 'rating']

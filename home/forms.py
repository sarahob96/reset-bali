from django.forms import ModelForm
from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Programme_attended': forms.TextInput(attrs={'class': 'form-control'}),
            'your_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

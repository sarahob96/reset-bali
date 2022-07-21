from django import forms
from .models import rewind


class rewind_form(forms.ModelForm):
    """
    """
    class Meta:
        model = rewind
        fields = ['name', 'programme_attended', 'date', 'email', 'phone']
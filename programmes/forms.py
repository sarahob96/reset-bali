from django import forms
from .models import rewind

class rewind_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(rewind_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = rewind
        fields = ['user', 'programme', 'date', 'email', 'phone']
from django import forms
from .models import rewind, renew, restart

class rewind_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(rewind_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = rewind
        fields = ['user', 'programme', 'date', 'email', 'phone']

class renew_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(renew_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = renew
        fields = ['user', 'programme', 'date', 'email', 'phone']


class restart_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(restart_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = restart
        fields = ['user', 'programme', 'date', 'email', 'phone']


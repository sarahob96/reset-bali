from django import forms
from .models import Rewind, Renew, Restart


class Rewind_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(Rewind_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Rewind
        fields = ['user', 'programme', 'date', 'email', 'phone']


class Renew_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(Renew_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Renew
        fields = ['user', 'programme', 'date', 'email', 'phone']


class Restart_form(forms.ModelForm):
    """
    """

    def __init__(self, *args, **kwargs):
       super(Restart_form, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Restart
        fields = ['user', 'programme', 'date', 'email', 'phone']


from django import forms
from .models import login, newUser


class LoginForm(forms.ModelForm):

    class Meta:
        model = login
        fields = ['userName', 'userPassword']


class Register(forms.ModelForm):

    class Meta:
        model = newUser
        fields = ['userName', 'email', 'userPassword', 'userPasswordRepeat']
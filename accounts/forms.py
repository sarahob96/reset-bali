from django import forms
from .models import login, newUser


class LoginForm(forms.ModelForm):

    userPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = login
        fields = ['userName', 'userPassword']


class Register(forms.ModelForm):

    userPassword = forms.CharField(widget=forms.PasswordInput)
    userPasswordRepeat = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = newUser
        fields = ['userName', 'email', 'userPassword', 'userPasswordRepeat']
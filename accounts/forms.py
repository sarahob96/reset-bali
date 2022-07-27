from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
   
    class Meta:

        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
        }
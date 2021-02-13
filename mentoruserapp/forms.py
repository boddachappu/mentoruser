from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(UserCreationForm):
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email',]



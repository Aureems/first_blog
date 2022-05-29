from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=False)
    email = forms.CharField(help_text=False)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text=False, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text=False, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
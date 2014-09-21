from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

class LogIn(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(widget = forms.PasswordInput)
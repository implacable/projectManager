from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from user_auth.models import MyUser

class LogIn(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(widget = forms.PasswordInput)


class CreateUser(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name','email',
                'password', 'password_confirmation')

    def save(self, commit=True):
        user = super(RegisterProfile, self).save()
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
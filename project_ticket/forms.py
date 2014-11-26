from django import forms
from django.forms import ModelForm


class EditInfo(forms.Form):
	firstname = forms.CharField(label = "First Name")
	lastname = forms.CharField(label = "Last Name")
	email = forms.EmailField(label = "Email")

	
class EditPassword(forms.Form):
	old_password = forms.CharField(widget=forms.PasswordInput(), label = "Old Password")
	new_password = forms.CharField(widget=forms.PasswordInput(), label = "New Password")
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label = "Confirm New Password")


class AddComment(ModelForm):
	pass
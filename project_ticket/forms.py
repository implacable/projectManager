from django import forms


class EditInfo(forms.Form):
	firstname = forms.CharField(label = "First Name")
	lastname = forms.CharField(label = "Last Name")
	email = forms.EmailField(label = "Email")
	

class EditPassword(forms.Form):
	new_password = forms.CharField(widget=forms.PasswordInput(), label = "New Password")
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label = "Confirm Password")
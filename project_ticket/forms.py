from django import forms
<<<<<<< HEAD
from django.forms import ModelForm
=======
from project_ticket.models import Project
from user_auth.models import MyUser
from project_ticket.models import Ticket
>>>>>>> 05fcef9ce97e7da83f8399f10af487361257fb57


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


class AddTicket(forms.Form):
	ticket = Ticket()
	name = forms.CharField(label = "Name")
	description = forms.CharField(label = "Description", widget = forms.Textarea)
	project = forms.ModelChoiceField(queryset=Project.objects.all())
	developer = forms.ModelMultipleChoiceField(queryset=MyUser.objects.all().filter(perm="developer"))
	status = forms.ChoiceField(label = 'Ticket Status', choices=ticket.ticket_statuss)


from django import forms
from django.forms import ModelForm
from project_ticket.models import Project, Ticket
from user_auth.models import MyUser


class EditInfo(forms.Form):
    firstname = forms.CharField(label = "First Name")
    lastname = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Email")


class EditPassword(forms.Form):
	old_password = forms.CharField(widget=forms.PasswordInput(), label = "Old Password")
	new_password = forms.CharField(widget=forms.PasswordInput(), label = "New Password")
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label = "Confirm New Password")


class AddComment(forms.Form):
	comment = forms.CharField(widget=forms.Textarea)


class AddTicket(forms.Form):
	ticket = Ticket()
	name = forms.CharField(label = "Name")
	description = forms.CharField(label = "Description", widget = forms.Textarea)
	project = forms.ModelChoiceField(queryset=Project.objects.all())
	developer = forms.ModelMultipleChoiceField(queryset=MyUser.objects.all().filter(perm="developer"))
	status = forms.ChoiceField(label = 'Ticket Status', choices=ticket.ticket_statuss)


class AddProject(forms.Form):
	name = forms.CharField(label = "Name")
	description = forms.CharField(label = "Description", widget = forms.Textarea)
	client = forms.ModelChoiceField(queryset=MyUser.objects.filter(perm="client"))
	project_manager = forms.ModelMultipleChoiceField(queryset=MyUser.objects.filter(perm="project_manager"))
	developer = forms.ModelMultipleChoiceField(queryset=MyUser.objects.filter(perm="developer"))


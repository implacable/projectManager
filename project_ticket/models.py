from django.db import models
from user_auth.models import MyUser
from datetime import datetime


class Project(models.Model):
	client = models.OneToOneField(MyUser, related_name = 'client')
	project_manager = models.ManyToManyField(MyUser, related_name = 'project_manager')
	project_name = models.CharField(max_length=32)
	description = models.TextField(max_length=256, default="")
	project_due = models.DateField(blank=True, null=True)


class Ticket(models.Model):
	developer = models.ManyToManyField(MyUser, related_name = 'developer')
	project = models.ForeignKey(Project, related_name = 'project')
	name = models.CharField(max_length=32)
	description_ticket = models.TextField(max_length = 1024, default="")
	date_completed = models.DateTimeField(blank = True, null = True)
	date_created = models.DateTimeField(default = datetime.now)

from django.db import models
from user_auth.models import MyUser
from datetime import datetime


class Project(models.Model):
	client = models.OneToOneField(MyUser, related_name = 'client')
	developer = models.ManyToManyField(MyUser, related_name='assigned_developers')
	project_manager = models.OneToOneField(MyUser, related_name = 'project_manager')
	project_name = models.CharField(max_length=32)
	description = models.TextField(max_length=256, default="")
	project_due = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.project_name


class Ticket(models.Model):
	developer = models.ManyToManyField(MyUser, related_name = 'developer')
	project = models.ForeignKey(Project, related_name = 'project')
	name = models.CharField(max_length=32)
	description_ticket = models.TextField(max_length = 1024, default="")
	date_completed = models.DateTimeField(blank = True, null = True)
	date_created = models.DateTimeField(default = datetime.now)

	# Set of choices for tickets
	# Back logged tickets are kept for records
	ticket_statuss = (
		('queued', 'Queued'),
		('in_progress', 'In Progress'),
		('testing', 'Testing'),
		('completed', 'Completed'),
		('back_log', 'Back Log'),
	)
	status = models.CharField(max_length=32, blank=True, null=True, choices=ticket_statuss)
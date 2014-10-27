from django.db import models
from user_auth.models import MyUser
from datetime import datetime


class Project(models.Model):
	client = models.OneToOneField(MyUser, related_name = 'client')
	project_manager = models.ManyToManyField(MyUser, related_name = 'project_manager')
	developer = models.ManyToManyField(MyUser, related_name = 'assigned_developer')
	name = models.CharField(max_length=32)
	description = models.TextField(max_length=256, default="")
	project_due = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.project_name


class Ticket(models.Model):
	project = models.ForeignKey(Project, related_name = 'project')
	developer = models.ManyToManyField(MyUser, related_name = 'developer')
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


class Activity_Feed(models.Models):
    project = models.ForeignKey(Project)
    date_edited = models.DateTimeField(default= datetime.now)


class Activity_feed_action(models,Models):
    activityFeed = models.ForeignKey(Activity_Feed)
    action_date = models.DateTimeField(default= datetime.now)

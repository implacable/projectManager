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
		return self.name


class Ticket(models.Model):
	# Changed related name from project to tickets - J
	project = models.ForeignKey(Project, related_name = 'tickets')
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

# Insert Comment Class here!
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket)
    text = models.TextField(max_length = 1024)
    date_submitted = models.DateTimeField(default = datetime.now)
    user = models.CharField(max_length = 120)

    # User should not have to input their name again.
    # Process should be sent to view.

    #def save(self):
     #   self.user = request.user.full_name()
      #  super(Comment, self).save()

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

	def save(self):
		action = ActionReport()
		new = self
		action.name = self.name
		action.save(new,"project")
		super(Project, self).save()


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
		('Queued', 'Queued'),
		('In Progress', 'In Progress'),
		('Testing', 'Testing'),
		('Completed', 'Completed'),
		('Back Log', 'Back Log'),
	)

	status = models.CharField(max_length=32, blank=True, null=True, choices=ticket_statuss)

	def save(self):
		action = ActionReport()
		action.project = self.project
		new = self
		action.save(new,"ticket")
		super(Ticket, self).save()

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


class ActionReport(models.Model):
    project = models.ForeignKey(Project, related_name="projects")
    message = models.CharField(max_length= 32, default=" ")

# Not sure about this implementation/logic but it works
# possible fix: default status of ticket is None
# need to do: figure out how to add a verb when ticket is deleted
# 			  figure out how to log the user who change the ticket
    def create_msg(self,new,md):
    	if md == "ticket":
    		if new.pk is not None:
    			old = Ticket.objects.get(pk=new.pk)
    			if old.status != new.status:
	    			verb = " changed %s from %s to %s on " % (new.name, old.status, new.status)
    			if old.name != new.name:
	    			verb = " change %s name to %s on "
    		else:
	    		verb =  " added %s to %s on %s" % (new.name,new.status,datetime.now())
		if md == "project":
			if new.pk is not None:
				old = Project.objects.get(pk=new.pk)
				if old.name != new.name or old.description != new.description:
					verb = " modified %s on " % (new.name)
    	self.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M.")
    def save(self,new,md):
    	self.create_msg(new,md)
    	super(ActionReport, self).save()


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
	recent_user = models.CharField(max_length = 120, default=" ")

	def __unicode__(self):
		return self.name

	def save(self):
		action = ActionReport()
		action.project = self
		if self.pk is not None:
			old = Project.objects.get(pk=self.pk)
			if self.name != old.name or self.description != old.description or self.project_due != old.project_due:
				verb ="%s edited %s on " % (self.recent_user,old.name)
				action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %H:%M")
				action.save()
		super(Project, self).save()


class Ticket(models.Model):
	# Changed related name from project to tickets - J
	project = models.ForeignKey(Project, related_name = 'tickets')
	developer = models.ManyToManyField(MyUser, related_name = 'developer')
	name = models.CharField(max_length=32)
	description_ticket = models.TextField(max_length = 1024, default="")
	date_completed = models.DateTimeField(blank = True, null = True)
	date_created = models.DateTimeField(default = datetime.now)
	recent_user = models.CharField(max_length = 120, default =" ")

	# Set of choices for tickets
	# Back logged tickets are kept for records
	ticket_statuss = (
		('Queued', 'Queued'),
		('In Progress', 'In Progress'),
		('Testing', 'Testing'),
		('Completed', 'Completed'),
		('Back Log', 'Back Log'),
	)

	status = models.CharField(max_length=32, default='Queued', choices=ticket_statuss)

	def save(self):
		action = ActionReport()
		action.project = self.project
		if self.pk is not None:
			old = Ticket.objects.get(pk=self.pk)
			if old.status != self.status:
				verb = "%s changed %s from %s to %s on " % (self.recent_user,self.name, old.status, self.status)
				action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %H:%M")
				action.save()
			if old.name != self.name or old.description_ticket != self.description_ticket:
				verb = "%s edited %s on " % (self.recent_user,self.name)
				action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %H:%M")
				action.save()
			
		else:
			verb =  "%s added %s to %s in %s on " % (self.recent_user,self.name,self.status,self.project.name)    	
			action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %H:%M")
			action.save()
		super(Ticket, self).save()


# Insert Comment Class here!
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket)
    text = models.TextField(max_length = 1024)
    date_submitted = models.DateTimeField(default = datetime.now)
    recent_user = models.CharField(max_length = 120, default=" ")

    def save(self):
    	action = ActionReport()
    	action.project = self.ticket.project
    	if self.pk is not None:
    		old = Comment.objects.get(pk=self.pk)
    		if (old.text != self.text or old.date_submitted != self.date_submitted 
    			or self.user != old.user or old.ticket != self.ticket):
    			verb = "%s edited comment on %s on " % (self.recent_user, self.ticket.name)
    			action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %H:%M")
    			action.save()
    			super(Comment,self).save()

    	else:
    		verb = "%s commented on %s on " % (self.recent_user, self.ticket.name)
    		action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %H:%M")
    		action.save()
    		super(Comment,self).save()

    # User should not have to input their name again.
    # Process should be sent to view.

    #def save(self):
     #   self.user = request.user.full_name()
      #  super(Comment, self).save()


class ActionReport(models.Model):
    project = models.ForeignKey(Project, related_name="projects")
    message = models.CharField(max_length= 32, default=" ")

    def save(self):
    	super(ActionReport, self).save()


from django.db import models
from user_auth.models import MyUser
from datetime import datetime

#	Needs Attention: Deleted create_msg function and moved its
# 						implementation to save functions.(Why?)

#						*Deleted create_msg() because it was no longer relevant as it 
#							contained only 1 line of code and can implement that code
#							to save() function
#					 	*By doing above, was able to create an ActionReport object
#							for Project and Ticket when its instances were changed
#					 	*Was able the remove the extra parameter from the save function
#						*Was able to create ActionReport objects for Project and Ticket
#							even when both were modified at the same time
#					This new implementation might be silly or hacky?

#			 To do:	
#					1. Implement save override in Comments
#					2. Changed variable names to something more descriptive
#						i.e. old,verb,new
#					3. Check the logic of save() in Project
#					4. Improve the verb(s) values(message)
#				*	5. Error with line 41 when creating a new project
#					6. Refactor
#					7. Delete this comment after ActionReport is fully functional on
#						all models
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
		if self.pk is not None:
			action.project = Project.objects.get(pk=self.pk)
			old = Project.objects.get(pk=self.pk)
			if self.name != old.name or self.description != old.description:
				verb =" modified %s " % (old.name)
				action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M.")
				action.save()
				super(Project, self).save()
		elif not self.pk:
			verb = " created %s" % (self.name)
			action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M.")
			super(Project, self).save()
#	action.message =... and action.save() and super(Project...) lines were moved and duplicated for the if/else statement to 
#	cover the instance when the user click save even if the user did not change any information
#	Otherwise: There will be a variable error "verb was referenced before assignment"

#	To do: When creating a new project there is an error with action.sav


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
		if self.pk is not None:
			old = Ticket.objects.get(pk=self.pk)
			if old.status != self.status:
				verb = " changed %s from %s to %s on " % (self.name, old.status, self.status)
			if old.name != self.name:
				verb = " change %s name to %s on " % (old.name,self.name)
		else:
			verb =  " added %s to %s in %s on " % (self.name,self.status,self.project.name)    	
		action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M.")
		action.save()
		super(Ticket, self).save()

# Insert Comment Class here!
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket)
    text = models.TextField(max_length = 1024)
    date_submitted = models.DateTimeField(default = datetime.now)
    user = models.CharField(max_length = 120)

    def save(self):
    	action = ActionReport()
    	action.project = self.ticket.project
    	if self.pk is not None:
    		old = Comment.objects.get(pk=self.pk)
    		if old.text != self.text:
    			verb = " edited comment on %s on " % (self.ticket.name)
    			action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M")
	    		action.save()
    			super(Comment, self).save()
    	else:
    		verb = " commented on %s on " % (self.ticket.name)
    		action.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M")
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

#################	This is the old implementation fo create_msg()	#################
#    def create_msg(self,verb):
#    	if md == "ticket":
#    		if new.pk is not None:
#				old = Ticket.objects.get(pk=new.pk)
#				if old.status != new.status:
#					verb = " changed %s from %s to %s on " % (new.name, old.status, new.status)
#				if old.name != new.name:
#					verb = " change %s name to %s on " % (old.name,new.name)
#				if old.project.name != new.project.name:
#					verb = "111"	
#    		else:
#	    		verb =  " added %s to %s in %s on " % (new.name,new.status,new.project.name)    	
#			if new.pk is not None:
#				old = Project.objects.get(pk=new.pk)
#				if old.name != new.name:
#					verb = " modified %s" % (old.name)
#			else:
#				verb = " created a project"		
#		self.message = verb + "%s" % (datetime.now()).strftime(" %B %d, %Y at %l:%M.")
#######################################################################################
    def save(self):
    	#self.create_msg(verb)
    	super(ActionReport, self).save()


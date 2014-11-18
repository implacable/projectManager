from django.contrib import admin
from project_ticket.models import Project, Ticket, Comment


# Register your models here.
class TicketInline(admin.TabularInline):
	model = Ticket
	extra = 0

class TicketComment(admin.ModelAdmin):
	fieldsets = [
		('None',			{'fields':['user']}),
		('Ticket',			{'fields':['ticket']}),
		('Date commented',	{'fields':['date_submitted']}),
		('Comment',			{'fields':['text']}),
	]
	
class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
	         ('None',                {'fields': ['name']}),
	         ('Project Description', {'fields': ['description'], 'classes': ['collapse']}),
	         ('Client',              {'fields': ['client']}),
	         ('Project Manager',     {'fields': ['project_manager']}),
	         ('Developers',              {'fields': ['developer']}),
	         ('Project Due',         {'fields': ['project_due']}),
	     ]
	inlines = [TicketInline]
	

admin.site.register(Project,ProjectAdmin)
admin.site.register(Comment,TicketComment)
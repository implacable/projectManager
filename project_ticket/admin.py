from django.contrib import admin
from project_ticket.models import Project, Ticket, Comment, ActionReport


# Register your models here.
class TicketInline(admin.TabularInline):
    fieldsets = [
        ('Whatever I want', {'fields': [
                               'name'
                             , 'description_ticket'
                             , 'date_created'
                             , 'date_completed'

        ]})]
    model = Ticket
    extra = 0

class TicketComment(admin.ModelAdmin):
    fieldsets = [
        ('Ticken Info', {'fields': [
                           'ticket'
                         , 'date_submitted'
                         , 'text']})]

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': [
                'name'
                , 'description'
                , 'client'
                , 'project_manager'
                , 'developer'
                , 'project_due']})]

    inlines = [TicketInline]


class AdminActionReport(admin.ModelAdmin):
    list_display = ('message',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, TicketComment)
admin.site.register(ActionReport, AdminActionReport)

from django.db import models
from user_auth.models import MyUser


class Project(models.Model):
    client = models.ManyToManyField(MyUser)
    #project_manager = models.ForeignKey(MyUser)
    name_project = models.CharField(max_length=32)
    project_due = models.DateField(blank=True, null=True)
    project_description = models.CharField(max_length=256)


class Ticket(models.Model):
    developer = models.ManyToManyField(MyUser)
    project = models.ForeignKey(Project)
    date_created = models.DateTimeField('Date Added')
    comment_ticket = models.CharField(max_length=256)
    name_ticket = models.CharField(max_length=32)


from django.db import models
from user_auth.models import MyUser


class Project(models.Model):
    client = models.OneToOneField(MyUser, related_name = 'user_client')
    project_manager = models.ManyToManyField(MyUser, related_name = 'user_project_manager')
    project_name = models.CharField(max_length=32)
    project_due = models.DateField(blank=True, null=True)
    description_of_project = models.TextField(max_length=256)


class Ticket(models.Model):
    developer = models.ManyToManyField(MyUser)
    project = models.ForeignKey(Project)
    date_created = models.DateField('Date Added')
    name_ticket = models.CharField(max_length=32)


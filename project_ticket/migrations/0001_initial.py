# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=32)),
                ('description', models.TextField(default=b'', max_length=256)),
                ('project_due', models.DateField(null=True, blank=True)),
                ('client', models.OneToOneField(related_name=b'client', to=settings.AUTH_USER_MODEL)),
                ('developer', models.ManyToManyField(related_name=b'assigned_developers', to=settings.AUTH_USER_MODEL)),
                ('project_manager', models.OneToOneField(related_name=b'project_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description_ticket', models.TextField(default=b'', max_length=1024)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(blank=True, max_length=32, null=True, choices=[(b'queued', b'Queued'), (b'in_progress', b'In Progress'), (b'testing', b'Testing'), (b'completed', b'Completed'), (b'back_log', b'Back Log')])),
                ('developer', models.ManyToManyField(related_name=b'developer', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(related_name=b'project', to='project_ticket.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

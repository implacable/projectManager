# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project_ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='name_ticket',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description_of_project',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_completed',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='description_ticket',
            field=models.TextField(default=b'', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'queued', b'Queued'), (b'in_progress', b'In Progress'), (b'testing', b'Testing'), (b'completed', b'Completed'), (b'back_log', b'Back Log')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.OneToOneField(related_name=b'client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ManyToManyField(related_name=b'project_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='developer',
            field=models.ManyToManyField(related_name=b'developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(related_name=b'project', to='project_ticket.Project'),
        ),
    ]

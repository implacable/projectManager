# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project_ticket', '0006_auto_20141122_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionreport',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionreport',
            name='project',
            field=models.ForeignKey(related_name=b'action_reports', to='project_ticket.Project'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(related_name=b'comments', to='project_ticket.Ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(related_name=b'tickets', to='project_ticket.Project'),
        ),
    ]

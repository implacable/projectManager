# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project_ticket', '0003_auto_20141017_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=1024)),
                ('date_submitted', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.CharField(max_length=120)),
                ('ticket', models.ForeignKey(to='project_ticket.Ticket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_ticket', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(default=b' ', max_length=1024)),
                ('project', models.ForeignKey(related_name=b'projects', to='project_ticket.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

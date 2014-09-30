# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


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
                ('project_due', models.DateField(null=True, blank=True)),
                ('description_of_project', models.TextField(max_length=256)),
                ('client', models.OneToOneField(related_name=b'user_client', to=settings.AUTH_USER_MODEL)),
                ('project_manager', models.ManyToManyField(related_name=b'user_project_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(verbose_name=b'Date Added')),
                ('name_ticket', models.CharField(max_length=32)),
                ('developer', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='project_ticket.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

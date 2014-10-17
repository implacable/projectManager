# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_auto_20140917_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_developer',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_project_manager',
        ),
        migrations.AddField(
            model_name='myuser',
            name='perm',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'client', b'Client'), (b'developer', b'Developer'), (b'project_manager', b'Project Manager')]),
            preserve_default=True,
        ),
    ]

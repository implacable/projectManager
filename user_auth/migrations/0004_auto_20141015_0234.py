# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20141015_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='perm',
            field=models.CharField(blank=True, max_length=32, null=True, choices=[(b'client', b'Client'), (b'developer', b'Developer'), (b'project_manager', b'Project Manager')]),
        ),
    ]

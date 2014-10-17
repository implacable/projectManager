# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_ticket', '0002_auto_20141017_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='project',
            name='developer',
            field=models.ManyToManyField(related_name=b'assigned_developer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

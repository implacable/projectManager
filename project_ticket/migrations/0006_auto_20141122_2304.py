# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_ticket', '0005_actionreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='recent_user',
            field=models.CharField(default=b' ', max_length=120),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='recent_user',
            field=models.CharField(default=b' ', max_length=120),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='recent_user',
            field=models.CharField(default=b' ', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionreport',
            name='message',
            field=models.CharField(default=b' ', max_length=32),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(default=b'Queued', max_length=32, choices=[(b'Queued', b'Queued'), (b'In Progress', b'In Progress'), (b'Testing', b'Testing'), (b'Completed', b'Completed'), (b'Back Log', b'Back Log')]),
        ),
    ]

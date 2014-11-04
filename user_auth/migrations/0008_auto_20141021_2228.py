# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_auto_20141021_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(default=b'', max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='contact',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]

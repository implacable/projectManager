# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20141021_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(default=b'', max_length=32),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='contact',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20141017_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(default=b'Address', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='contact',
            field=models.CharField(default=b'XXXXXXXXXX', max_length=10),
            preserve_default=True,
        ),
    ]

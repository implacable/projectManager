# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_auto_20141021_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='contact',
        ),
    ]

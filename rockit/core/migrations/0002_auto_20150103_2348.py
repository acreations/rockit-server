# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='action',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 23, 48, 31, 957654, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

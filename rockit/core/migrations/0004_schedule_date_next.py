# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150105_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date_next',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 15, 33, 59, 239074, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

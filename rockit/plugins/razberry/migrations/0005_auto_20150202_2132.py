# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('razberry', '0004_auto_20150202_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actionthen',
            name='command',
        ),
        migrations.RemoveField(
            model_name='actionthen',
            name='value',
        ),
        migrations.AddField(
            model_name='actionthen',
            name='criterias',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionthen',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 21, 32, 18, 247287, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]

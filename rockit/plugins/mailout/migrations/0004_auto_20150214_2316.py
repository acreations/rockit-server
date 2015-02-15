# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mailout', '0003_mailout_mailoutrecipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailout',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 22, 15, 57, 353783, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mailout',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 22, 16, 8, 937964, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

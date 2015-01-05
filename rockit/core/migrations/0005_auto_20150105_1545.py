# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_schedule_date_next'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date_next',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]

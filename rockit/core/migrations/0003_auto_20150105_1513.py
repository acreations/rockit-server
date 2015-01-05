# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150103_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='uuid',
            field=models.CharField(unique=True, max_length=36, blank=True),
            preserve_default=True,
        ),
    ]

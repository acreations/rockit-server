# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150105_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='entry',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]

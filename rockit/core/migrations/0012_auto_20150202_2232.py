# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150202_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionthen',
            name='identifier',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]

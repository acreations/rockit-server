# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150117_1457'),
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
            name='identifier',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

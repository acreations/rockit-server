# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('razberry', '0005_auto_20150202_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actionthen',
            name='criterias',
        ),
        migrations.AddField(
            model_name='actionthen',
            name='command',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionthen',
            name='value',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]

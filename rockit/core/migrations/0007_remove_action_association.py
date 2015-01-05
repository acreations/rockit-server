# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150105_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='association',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_hello'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

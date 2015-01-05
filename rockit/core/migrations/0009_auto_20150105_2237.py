# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_actionthen_holder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='done',
        ),
        migrations.AddField(
            model_name='schedule',
            name='action',
            field=models.ForeignKey(default=2, to='core.Action'),
            preserve_default=False,
        ),
    ]

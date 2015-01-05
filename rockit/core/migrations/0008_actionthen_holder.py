# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_action_association'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionthen',
            name='holder',
            field=models.ForeignKey(default=1, to='core.Action'),
            preserve_default=False,
        ),
    ]

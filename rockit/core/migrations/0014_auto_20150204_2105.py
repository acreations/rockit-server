# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_actionfinish_actionwhen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='action',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AlterField(
            model_name='actionfinish',
            name='target',
            field=models.ForeignKey(to='core.Association'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionthen',
            name='target',
            field=models.ForeignKey(to='core.Association'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actionwhen',
            name='target',
            field=models.ForeignKey(to='core.Association'),
            preserve_default=True,
        ),
    ]

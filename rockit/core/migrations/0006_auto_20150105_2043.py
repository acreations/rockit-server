# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150105_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionThen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('command', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=100)),
                ('target', models.ForeignKey(to='core.Node')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='action',
            name='aid',
        ),
        migrations.RemoveField(
            model_name='action',
            name='params',
        ),
    ]

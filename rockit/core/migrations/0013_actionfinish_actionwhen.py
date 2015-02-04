# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150202_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionFinish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=50)),
                ('holder', models.ForeignKey(to='core.Action')),
                ('target', models.ForeignKey(to='core.Node')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionWhen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=50)),
                ('holder', models.ForeignKey(to='core.Action')),
                ('target', models.ForeignKey(to='core.Node')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

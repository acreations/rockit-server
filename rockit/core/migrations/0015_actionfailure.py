# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150204_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionFailure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('holder', models.CharField(default=b'undefined', max_length=200)),
                ('identifier', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(to='core.Association')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

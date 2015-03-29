# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cron', models.CharField(max_length=50, blank=True)),
                ('repeat', models.BooleanField(default=False)),
                ('date_next', models.DateTimeField(blank=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

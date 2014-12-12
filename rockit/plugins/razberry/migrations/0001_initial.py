# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=100)),
                ('device_type', models.CharField(default=b'', max_length=50)),
                ('manufacturer_id', models.CharField(default=b'', max_length=50)),
                ('manufacturer_name', models.CharField(default=b'', max_length=50)),
                ('version', models.CharField(default=b'', max_length=10)),
                ('listening', models.BooleanField(default=False)),
                ('routing', models.BooleanField(default=False)),
                ('beaming', models.BooleanField(default=False)),
                ('awaken', models.BooleanField(default=False)),
                ('failed', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NodeCommand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('identifier', models.IntegerField()),
                ('namespace', models.CharField(default=b'', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('node', models.ForeignKey(to='razberry.Node')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NodeVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sdk', models.CharField(default=b'', max_length=16)),
                ('application', models.CharField(default=b'', max_length=16)),
                ('zw_library', models.IntegerField(default=0)),
                ('zw_protocol', models.CharField(default=b'', max_length=16)),
                ('node', models.ForeignKey(to='razberry.Node')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('value', models.CharField(max_length=100, blank=True)),
                ('readonly', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

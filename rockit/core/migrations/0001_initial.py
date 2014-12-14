# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def register_to_rockit(apps, schema_editor):

    Association = apps.get_model("core", "Association")

    association = Association()
    association.name            = "Rockit"
    association.description     = "All rockit core functionality"
    association.namespace       = "rockit.foundation.core"
    association.entry           = "rockit"
    association.when_addable    = True
    association.save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'undefined', max_length=200)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('aid', models.CharField(max_length=100, blank=True)),
                ('params', models.CharField(max_length=1000, blank=True)),
                ('favorite', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'undefined', max_length=200)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('namespace', models.CharField(max_length=100)),
                ('entry', models.CharField(max_length=100)),
                ('addable', models.BooleanField(default=False)),
                ('when_addable', models.BooleanField(default=False)),
                ('then_addable', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=36, blank=True)),
                ('name', models.CharField(default=b'undefined', max_length=200)),
                ('aid', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('association', models.ForeignKey(to='core.Association')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NodeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'undefined', max_length=50)),
                ('color', models.CharField(default=b'#000000', max_length=7)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cron', models.CharField(max_length=50, blank=True)),
                ('done', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('action', models.ForeignKey(to='core.Action')),
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
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=36, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='node',
            name='category',
            field=models.ForeignKey(default=None, blank=True, to='core.NodeCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='association',
            field=models.ForeignKey(to='core.Association'),
            preserve_default=True,
        ),
        migrations.RunPython(register_to_rockit),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_settings(apps, schema_editor):

    Setting = apps.get_model("mailout", "Setting")

    server = Setting()
    server.name = "SMTP_SERVER"
    server.description = "SMTP server ip address"
    server.save()

    port = Setting()
    port.name = "SMTP_PORT"
    port.description = "SMTP port port"
    port.value = "587"
    port.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mailout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('value', models.CharField(max_length=100, blank=True)),
                ('readonly', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RunPython(add_settings),
    ]

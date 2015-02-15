# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_settings(apps, schema_editor):

    Setting = apps.get_model("mailout", "Setting")

    server = Setting()
    server.name = "SENDER"
    server.description = "Sender"
    server.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mailout', '0002_setting'),
    ]

    operations = [
        migrations.RunPython(add_settings),
    ]

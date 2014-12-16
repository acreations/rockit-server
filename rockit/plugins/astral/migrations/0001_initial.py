# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def register_to_rockit(apps, schema_editor):

    Association = apps.get_model("core", "Association")

    association = Association()
    association.name        = "Astral"
    association.description = "Settings for astral to calculate Sunrise and Sunset"
    association.namespace   = "rockit.plugins.astral"
    association.entry       = "astral"
    association.addable     = True
    association.save()

class Migration(migrations.Migration):

    dependencies = [
      ('core', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(register_to_rockit),
    ]

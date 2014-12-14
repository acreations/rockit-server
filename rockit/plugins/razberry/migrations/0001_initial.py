# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def register_to_rockit(apps, schema_editor):

    Association = apps.get_model("core", "Association")

    association = Association()
    association.name        = "Razberry"
    association.description = "Communicate with Z-Wave devices using Razberry"
    association.namespace   = "rockit.plugins.razberry"
    association.entry       = "razberry"
    association.addable     = True
    association.save()

class Migration(migrations.Migration):

    dependencies = [
      ('core', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(register_to_rockit),
    ]

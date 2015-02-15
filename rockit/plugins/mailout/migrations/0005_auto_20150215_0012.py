# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailout', '0004_auto_20150214_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailoutrecipient',
            old_name='email',
            new_name='recipient',
        ),
    ]

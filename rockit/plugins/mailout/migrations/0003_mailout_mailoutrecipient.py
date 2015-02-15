# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailout', '0002_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=3000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailoutRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('mailout', models.ForeignKey(to='mailout.Mailout')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

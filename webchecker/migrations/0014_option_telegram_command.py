# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webchecker', '0013_customnotice'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='telegram_command',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webchecker', '0007_option_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='using_options',
            new_name='options',
        ),
    ]

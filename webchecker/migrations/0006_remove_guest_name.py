# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webchecker', '0005_auto_20170109_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='name',
        ),
    ]

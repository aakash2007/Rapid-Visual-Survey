# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0022_auto_20170617_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rc_building',
            name='bas_prsnt',
            field=models.NullBooleanField(verbose_name='Basement'),
        ),
    ]

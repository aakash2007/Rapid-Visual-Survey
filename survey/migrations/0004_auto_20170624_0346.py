# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20170624_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ms_building',
            name='pnding',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Absent'), (1, 'Normal Apparent Condition of Adjacent Building'), (2, 'Poor Apparent Condition of Adjacent Building')], verbose_name='Pounding'),
        ),
    ]

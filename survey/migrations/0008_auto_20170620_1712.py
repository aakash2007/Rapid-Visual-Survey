# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_rc_building_soil_cn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rc_building',
            name='frm_act',
            field=models.PositiveIntegerField(choices=[(0, 'Absent'), (1, 'Present')], default=0, verbose_name='Frame Action Present'),
            preserve_default=False,
        ),
    ]

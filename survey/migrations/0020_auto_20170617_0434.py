# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0019_auto_20170617_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='rc_building',
            name='op_bl_use',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='If Others, Specify'),
        ),
        migrations.AlterField(
            model_name='rc_building',
            name='bl_use',
            field=models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Mixed', 'Mixed'), ('Others', 'Others')], max_length=50, verbose_name='Building Use'),
        ),
    ]

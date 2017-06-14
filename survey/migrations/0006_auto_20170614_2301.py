# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20170614_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hy_building',
            options={'verbose_name': 'Hybrid Building', 'verbose_name_plural': 'Hybrid Buildings'},
        ),
        migrations.AlterModelOptions(
            name='ms_building',
            options={'verbose_name': 'Masonary Building', 'verbose_name_plural': 'Masonary Buildings'},
        ),
        migrations.AlterModelOptions(
            name='rc_building',
            options={'verbose_name': 'RC Building', 'verbose_name_plural': 'RC Buildings'},
        ),
        migrations.AlterField(
            model_name='rc_building',
            name='bl_id',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, verbose_name='Building ID'),
        ),
        migrations.AlterField(
            model_name='rc_building',
            name='uniq',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='rc_building',
            name='yr_extn',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Year of Extension(If Any)'),
        ),
    ]
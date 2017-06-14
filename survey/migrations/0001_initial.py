# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bl_id', models.PositiveIntegerField()),
                ('addr', models.CharField(max_length=200)),
                ('gps_x', models.DecimalField(decimal_places=7, max_digits=10)),
                ('gps_y', models.DecimalField(decimal_places=7, max_digits=10)),
                ('oc_day', models.PositiveIntegerField()),
                ('oc_night', models.PositiveIntegerField()),
                ('no_floor', models.PositiveSmallIntegerField()),
                ('yr_constr', models.PositiveSmallIntegerField(max_length=4)),
                ('yr_extn', models.PositiveSmallIntegerField(blank=True, max_length=4)),
                ('acc_level', models.CharField(max_length=10)),
                ('bl_use', models.CharField(max_length=50)),
                ('s_zone', models.PositiveIntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_text', models.CharField(max_length=50)),
                ('q_ans', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_st', models.BooleanField(default=False)),
                ('op_park_grnd', models.BooleanField()),
                ('abs_prt_walls', models.BooleanField()),
                ('st_for_comm', models.BooleanField()),
                ('tl_ht_grnd', models.BooleanField()),
                ('vrt_irrg', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_1', models.CharField(max_length=50)),
                ('mem_2', models.CharField(blank=True, max_length=50)),
                ('mem_3', models.CharField(blank=True, max_length=50)),
                ('mem_4', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survey.Team'),
        ),
    ]
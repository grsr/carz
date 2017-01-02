# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(blank=True, max_length=256, null=True)),
                ('variant', models.CharField(blank=True, max_length=256, null=True)),
                ('img_url', models.URLField(blank=True, max_length=256, null=True)),
                ('average_mpg', models.IntegerField(blank=True, null=True)),
                ('co2_emissions_combined', models.IntegerField(blank=True, null=True)),
                ('co2_tax_band', models.CharField(blank=True, max_length=8, null=True)),
                ('road_tax_year_1', models.IntegerField(blank=True, null=True)),
                ('road_tax_annual', models.IntegerField(blank=True, null=True)),
                ('insurance_group', models.CharField(blank=True, max_length=8, null=True)),
                ('warranty_duration', models.IntegerField(blank=True, null=True)),
                ('engine_size', models.IntegerField(blank=True, null=True)),
                ('fuel', models.CharField(blank=True, max_length=32, null=True)),
                ('gearbox', models.CharField(blank=True, max_length=64, null=True)),
                ('top_speed', models.IntegerField(blank=True, null=True)),
                ('tank_range', models.IntegerField(blank=True, null=True)),
                ('nought_to_sixty', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('max_power', models.IntegerField(blank=True, null=True)),
                ('max_torque', models.IntegerField(blank=True, null=True)),
                ('body_type', models.CharField(blank=True, max_length=64, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('seats', models.IntegerField(blank=True, null=True)),
                ('luggage_capacity_seats_up', models.IntegerField(blank=True, null=True)),
                ('luggage_capacity_seats_down', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
    ]

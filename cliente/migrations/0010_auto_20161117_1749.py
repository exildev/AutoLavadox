# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 17:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_auto_20161103_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='kilometraje',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='identificacion',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^([1-9]+[0-9]*){7,20}$'), 'Identificacion no valida', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

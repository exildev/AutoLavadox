# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0005_auto_20181105_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ventas_sin_existencias',
            field=models.BooleanField(default=False, verbose_name='Ventas sin existencias para la operacion'),
        ),
    ]

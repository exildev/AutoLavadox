# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0003_auto_20170824_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='inventario',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ventas_sin_existencias',
            field=models.BooleanField(default=False, verbose_name='Facturas sin '),
        ),
    ]

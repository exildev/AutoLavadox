# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_cierre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cierre',
            options={'verbose_name': 'Cierre de Inventario', 'verbose_name_plural': 'Cierres de Inventario'},
        ),
    ]

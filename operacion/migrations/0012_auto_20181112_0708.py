# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0011_auto_20181111_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Operacion'),
        ),
    ]

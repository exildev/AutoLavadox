# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_auto_20181106_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Operacion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
        ),
    ]

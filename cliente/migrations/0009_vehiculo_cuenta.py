# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0014_auto_20181120_0248'),
        ('cliente', '0008_auto_20181112_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subcripcion.Cuenta'),
        ),
    ]

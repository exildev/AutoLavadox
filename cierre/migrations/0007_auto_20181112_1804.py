# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cierre', '0006_auto_20181112_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierre',
            name='turno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cierre.Turno'),
        ),
    ]
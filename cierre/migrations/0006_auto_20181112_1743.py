# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cierre', '0005_auto_20170828_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cierre', '0007_auto_20181112_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierre',
            name='fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cierre',
            name='inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
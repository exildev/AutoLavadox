# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0008_auto_20181112_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suscripcion',
            name='inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
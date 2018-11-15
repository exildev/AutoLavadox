# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 23:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0025_auto_20181112_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Operacion'),
        ),
        migrations.AlterField(
            model_name='tiposervicio',
            name='costo',
            field=models.FloatField(default=0, validators=[django.core.validators.RegexValidator(re.compile('^[1-9]+[0-9]*.[0-9]+[0-9]*|[1-9]+[0-9]*$'), 'Costo no valido', 'invalid')]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operacion', '0027_auto_20161006_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiemposOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacion.Orden')),
            ],
        ),
    ]
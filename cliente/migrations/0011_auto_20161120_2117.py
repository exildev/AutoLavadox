# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_auto_20161117_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialKilometraje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometraje', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Historial de Kilometraje',
                'verbose_name_plural': 'Historial de Kilometraje',
            },
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='kilometraje',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historialkilometraje',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Vehiculo'),
        ),
    ]
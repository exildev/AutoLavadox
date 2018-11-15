# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0017_auto_20181112_2309'),
        ('operacion', '0032_auto_20181114_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaDeServicioOperacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacion.Orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Venta')),
            ],
        ),
        migrations.AlterField(
            model_name='componente',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Operacion'),
        ),
    ]

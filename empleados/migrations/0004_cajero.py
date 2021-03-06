# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 20:08
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_recepcionista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empleados.Persona')),
            ],
            options={
                'verbose_name': 'Cajero',
                'verbose_name_plural': 'Cajeros',
            },
            bases=('empleados.persona',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

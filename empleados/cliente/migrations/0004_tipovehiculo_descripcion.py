# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20161005_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipovehiculo',
            name='descripcion',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
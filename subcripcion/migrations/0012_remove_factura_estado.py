# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-15 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0011_auto_20181115_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='estado',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-14 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20180814_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datauncertainty',
            name='qbc',
            field=models.FloatField(null=True),
        ),
    ]

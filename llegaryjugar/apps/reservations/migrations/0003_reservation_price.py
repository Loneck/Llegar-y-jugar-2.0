# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-30 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20170714_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True, verbose_name='price'),
        ),
    ]

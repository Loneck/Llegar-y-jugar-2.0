# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-18 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_status', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations_status',
            new_name='ReservationsStatus',
        ),
    ]
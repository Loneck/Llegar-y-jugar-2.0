# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationsStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Reservada'), (1, 'Confirmada')], default=0, verbose_name='estado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

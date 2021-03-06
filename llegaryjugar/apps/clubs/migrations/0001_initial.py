# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('mail', models.EmailField(max_length=254)),
                ('logo', models.ImageField(upload_to=b'clubs/logo/', verbose_name='image')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=20, verbose_name='latitude')),
                ('length', models.DecimalField(decimal_places=6, max_digits=20, verbose_name='length')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

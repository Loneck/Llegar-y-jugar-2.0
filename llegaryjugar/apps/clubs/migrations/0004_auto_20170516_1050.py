# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20170504_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='description',
            field=models.TextField(verbose_name='descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='logo',
            field=models.ImageField(upload_to=b'clubs/logo/', verbose_name='image'),
        ),
    ]
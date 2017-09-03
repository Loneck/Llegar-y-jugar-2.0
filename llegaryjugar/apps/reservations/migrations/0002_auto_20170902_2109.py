# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 00:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created Date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='payment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='res_payment', to='payment_methods.PaymentMethod', verbose_name='payment'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='res_reservationsStatus', to='reservations_status.ReservationsStat', verbose_name='reservations Status'),
        ),
    ]
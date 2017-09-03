# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 00:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations_status', '0001_initial'),
        ('payment_methods', '0001_initial'),
        ('schedules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0001_initial'),
        ('courts', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30, null=True, verbose_name='price')),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created Date')),
                ('client', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_name', to='clubs.Club')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_courts', to='courts.Court', verbose_name='courts')),
                ('payment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='res_payment', to='payment_methods.PaymentMethod', verbose_name='payment')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_schedule', to='schedules.Schedule', verbose_name='schedule')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_service', to='services.Service', verbose_name='service')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='res_reservationsStatus', to='reservations_status.ReservationsStat', verbose_name='reservations Status')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

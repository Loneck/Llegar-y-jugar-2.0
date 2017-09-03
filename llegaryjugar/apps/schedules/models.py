# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date

from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.courts.models import Court
from llegaryjugar.apps.dates.models import Day, Month, Hour


class Schedule(BaseModel):
    court = models.ForeignKey(
        Court,
        related_name='court_sche',
        verbose_name=_('court'),
    )
    price = models.DecimalField(
        _('price'),
        decimal_places=2,
        max_digits=30,
    )
    date = models.DateField(
        _('Date'),
        default=date.today
    )
    start_time = models.TimeField(
        _('start time'),
    )
    end_time = models.TimeField(
        _('end time'),
    )

    def __unicode__(self):
        return '{} {}'.format(
            self.start_time,
            self.end_time,
        )


class SchedulesCreate(BaseModel):
    author = models.ForeignKey(
        'auth.User',
        related_name='schedule_court',
        verbose_name=_('author'),
    )
    court = models.ForeignKey(
        Court,
        related_name='court_sche_create',
        verbose_name=_('court'),
        null=True,
    )
    price = models.DecimalField(
        _('price'),
        decimal_places=2,
        max_digits=30,
    )
    day = models.ManyToManyField(
        Day,
        related_name='day_create',
        verbose_name=_('day'),
    )
    month = models.ManyToManyField(
        Month,
        related_name='month_create',
        verbose_name=_('month'),
    )
    start_time = models.ForeignKey(
        Hour,
        related_name='start_time_hour',
        null=True
    )
    end_time = models.ForeignKey(
        Hour,
        related_name='end_time_hour',
        null=True
    )

    def day_in_month(self):
        days = self.day.values_list('day', flat=True)
        months = self.month.values_list('month', flat=True)

        return days, months

    def create_schedules(self):
        hour_format = "%H:%M"
        start_time = str(self.start_time)
        end_time = str(self.end_time)

        if end_time == '24:00':
            end_time = '23:59'
        start_time = datetime.strptime(start_time, hour_format)
        end_time = datetime.strptime(end_time, hour_format)

        schedule_list = []
        while start_time <= end_time:
            start_time.strftime(hour_format)
            schedule_list.append(start_time.strftime(hour_format))
            start_time += timedelta(minutes=60)

        midnight = end_time.strftime(hour_format)
        if midnight == '23:59':
            schedule_list.append('00:00')

        price = self.price
        court = self.court
        for start_time, end_time in zip(schedule_list, schedule_list[1:]):
            start = start_time
            end = end_time
            Schedule.objects.create(
                price=price,
                court=court,
                start_time=start,
                end_time=end,
            )

    def __unicode__(self):
        return '{} {}'.format(
            self.author.get_full_name(),
            self.court.name,
        )


@receiver(
    m2m_changed,
    sender=SchedulesCreate.day.through,
    dispatch_uid='day_schedule_create')
@receiver(
    m2m_changed,
    sender=SchedulesCreate.month.through,
    dispatch_uid='day_schedule_create')
def day_schedule_create(sender, instance, action, *args, **kwargs):
    if (action == 'post_add' and
            instance.day.exists() and instance.month.exists()):
        instance.create_schedules()

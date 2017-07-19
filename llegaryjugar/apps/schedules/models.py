# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.courts.models import Courts
from llegaryjugar.apps.dates.models import Day, Month, Hour
from datetime import datetime, timedelta, date


class Schedule(BaseModel):
    court = models.ForeignKey(Courts, related_name='court', verbose_name=_('court'))
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
    date = models.DateField(_("Date"), default=date.today)
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))


class SchedulesCreate(BaseModel):
    author = models.ForeignKey('auth.User')
    court = models.ForeignKey(Courts, related_name='court_sche_create', verbose_name=_('court'), default="Sin asignar")
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
    day = models.ManyToManyField(Day, verbose_name=_('day'))
    month = models.ManyToManyField(Month, verbose_name=_('month'))
    start_time = models.ForeignKey(Hour, related_name='start_time_hour', default=True)
    end_time = models.ForeignKey(Hour, related_name='end_time_hour', default=True)

    def create_schedules(self):
        format = "%H:%M"

        start_time = str(self.start_time)
        end_time = str(self.end_time)

        if end_time == '24:00':
            end_time = '23:59'
        start_time = datetime.strptime(start_time, format)
        end_time = datetime.strptime(end_time, format)

        schedule_list = []
        while start_time <= end_time:
            start_time.strftime(format)
            schedule_list.append(start_time.strftime(format))
            start_time += timedelta(minutes=60)

        midnight = end_time.strftime(format)
        if midnight == '23:59':
            schedule_list.append('00:00')

        price = self.price
        court = self.court

        for start_time, end_time in zip(schedule_list, schedule_list[1:]):
            start = start_time
            end = end_time

            Schedule.objects.create(price=price, start_time=start, end_time=end, court=court)

    def save(self, *args, **kwargs):
        self.create_schedules()
        super(SchedulesCreate, self).save(*args, **kwargs)

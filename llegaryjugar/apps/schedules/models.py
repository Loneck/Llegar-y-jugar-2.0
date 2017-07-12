# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.courts.models import Courts
from llegaryjugar.apps.dates.models import Day, Month, Hour
from datetime import datetime, timedelta, date

class Schedules(BaseModel):
	court = models.ForeignKey(Courts, related_name='court', verbose_name=_('court'))
	price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
	date = models.DateField(_("Date"), default=date.today)
	start_time = models.TimeField(_('start time'))
	end_time = models.TimeField(_('end time'))

class SchedulesCreate(BaseModel):
	author = models.ForeignKey('auth.User')
	price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
	day = models.ManyToManyField(Day, verbose_name=_('day'))
	month = models.ManyToManyField(Month, verbose_name=_('month'))
	start_time = models.ForeignKey(Hour, related_name='start_time', default=True)
	end_time = models.ForeignKey(Hour, related_name='end_time', default=True)

	def create_schedules():
		formato = '%H:%M'

		start_time = raw_input('Insert Start Time(hh:mm): ')
		end_time = raw_input('Insert End Time(hh:mm): ')	

		start_time = datetime.strptime(start_time, formato)
		end_time = datetime.strptime(end_time, formato)
		diferencia = end_time - start_time

		schedules_list=[]
		while start_time <= end_time:
			schedules_list.append(start_time)
			start_time += timedelta(minutes=60)

		return 0
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
	start_time = models.ForeignKey(Hour, related_name='start_time_hour', default=True)
	end_time = models.ForeignKey(Hour, related_name='end_time_hour', default=True)

	def create_schedules(self):
		format = '%H:%M'

		start_time = self.start_time
		end_time = self.end_time

		start_time = datetime.strptime(start_time, formato)
		end_time = datetime.strptime(end_time, formato)
		diferencia = end_time - start_time

		schedules_list = []
		while start_time <= end_time:
			schedules_list.extends(start_time)
			start_time += timedelta(minutes=60)

		
		for x in range(len(schedules_list)):
			if form.is_valid():
				meter_el_author_en = author_schedules
				meter_el_precio_en = price_schedules
				meter_el_star_time_en = start_time_schedules
				meter_el_precio_en = price_schedules

		return 0
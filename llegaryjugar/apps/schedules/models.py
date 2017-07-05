# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.courts.models import Courts
from llegaryjugar.apps.dates.models import Day, Month
import datetime

class Schedules(BaseModel):
	court = models.ForeignKey(Courts, related_name='court', verbose_name=_('court'))
	price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
	date = models.DateField(_("Date"), default=datetime.date.today)
	start_time = models.TimeField(_('start time'))
	end_time = models.TimeField(_('end time'))

class SchedulesCreate(BaseModel):
	author = models.ForeignKey('auth.User')
	price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
	day = models.ManyToManyField(Day, verbose_name=_('day'))
	month = models.ManyToManyField(Month, verbose_name=_('month'))

	

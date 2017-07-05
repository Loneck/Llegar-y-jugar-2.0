# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from django.db import models
import datetime, calendar

class Month(BaseModel):
	MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

	month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')

	def __unicode__(self):
		return u'%s' %(self.get_month_display())

class Day(BaseModel):
	DAY_MONDAY, DAY_TUESDAY, DAY_WEDNESDAY, DAY_THURSDAY, DAY_FRIDAY, DAY_SATURDAY, DAY_SUNDAY = range(1,8)
	DAY_CHOICES = (
		(DAY_MONDAY, _(u'Monday')),
		(DAY_TUESDAY, _(u'Tuesday')),
		(DAY_WEDNESDAY, _(u'Wednesday')),
		(DAY_THURSDAY, _(u'Thursday')),
		(DAY_FRIDAY, _(u'Friday')),
		(DAY_SATURDAY, _(u'Saturday')),
		(DAY_SUNDAY, _(u'Sunday'))
	)

	day = models.PositiveIntegerField(_('day'), choices=DAY_CHOICES, default='1')

	def __unicode__(self):
		return u'%s' %(self.get_day_display())

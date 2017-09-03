# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from django.db import models
import calendar


class Month(BaseModel):
    MONTH_CHOICES = [(i, calendar.month_name[i]) for i in range(1, 13)]

    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES,
        unique=True,
    )

    def __unicode__(self):
        return u'%s' % (self.get_month_display())


class Day(BaseModel):
    (DAY_MONDAY,
     DAY_TUESDAY,
     DAY_WEDNESDAY,
     DAY_THURSDAY,
     DAY_FRIDAY,
     DAY_SATURDAY,
     DAY_SUNDAY) = range(0, 7)

    DAY_CHOICES = (
        (DAY_MONDAY, _(u'Monday')),
        (DAY_TUESDAY, _(u'Tuesday')),
        (DAY_WEDNESDAY, _(u'Wednesday')),
        (DAY_THURSDAY, _(u'Thursday')),
        (DAY_FRIDAY, _(u'Friday')),
        (DAY_SATURDAY, _(u'Saturday')),
        (DAY_SUNDAY, _(u'Sunday'))
    )

    day = models.PositiveIntegerField(
        _('day'),
        choices=DAY_CHOICES,
        unique=True,
    )

    def __unicode__(self):
        return u'%s' % (self.get_day_display())


class Hour(BaseModel):
    (ONE_HOUR,
     TWO_HOUR,
     THREE_HOUR,
     FOUR_HOUR,
     FIVE_HOUR,
     SIX_HOUR,
     SEVEN_HOUR,
     EIGHT_HOUR,
     NINE_HOUR,
     TEN_HOUR,
     ELEVEN_HOUR,
     TWELVE_HOUR,
     THIRTEEN_HOUR,
     FOURTENN_HOUR,
     FIFTEEN_HOUR,
     SIXTEEN_HOUR,
     SEVENTEEN_HOUR,
     EIGHTEEN_HOUR,
     NINETEEN_HOUR,
     TWENTY_HOUR,
     TWENTY_ONE_HOUR,
     TWENTY_TWO_HOUR,
     TWENTY_THREE_HOUR,
     TWENTY_FOUR_HOUR) = range(1, 25)

    HOUR_CHOICES = (
        (ONE_HOUR, _(u'01:00')),
        (TWO_HOUR, _(u'02:00')),
        (THREE_HOUR, _(u'03:00')),
        (FOUR_HOUR, _(u'04:00')),
        (FIVE_HOUR, _(u'05:00')),
        (SIX_HOUR, _(u'06:00')),
        (SEVEN_HOUR, _(u'07:00')),
        (EIGHT_HOUR, _(u'08:00')),
        (NINE_HOUR, _(u'09:00')),
        (TEN_HOUR, _(u'10:00')),
        (ELEVEN_HOUR, _(u'11:00')),
        (TWELVE_HOUR, _(u'12:00')),
        (THIRTEEN_HOUR, _(u'13:00')),
        (FOURTENN_HOUR, _(u'14:00')),
        (FIFTEEN_HOUR, _(u'15:00')),
        (SIXTEEN_HOUR, _(u'16:00')),
        (SEVENTEEN_HOUR, _(u'17:00')),
        (EIGHTEEN_HOUR, _(u'18:00')),
        (NINETEEN_HOUR, _(u'19:00')),
        (TWENTY_HOUR, _(u'20:00')),
        (TWENTY_ONE_HOUR, _(u'21:00')),
        (TWENTY_TWO_HOUR, _(u'22:00')),
        (TWENTY_THREE_HOUR, _(u'23:00')),
        (TWENTY_FOUR_HOUR, _(u'24:00'))
    )

    hour = models.PositiveIntegerField(
        _('hour'),
        choices=HOUR_CHOICES,
    )

    def __unicode__(self):
        return u'%s' % (self.get_hour_display())

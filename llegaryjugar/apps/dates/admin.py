# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Day, Month

@admin.register(Month)
class MonthAdmin(BaseAdmin):
    list_display = ('month',)

@admin.register(Day)
class DayAdmin(BaseAdmin):
    list_display = ('day',)
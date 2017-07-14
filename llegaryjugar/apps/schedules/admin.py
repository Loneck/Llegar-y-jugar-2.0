# -*- coding: utf-8 -*-
from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Schedules, SchedulesCreate

@admin.register(Schedules)
class SchedulesAdmin(BaseAdmin):
    list_display = ('court','date','start_time','end_time')

@admin.register(SchedulesCreate)
class SchedulesCreateAdmin(BaseAdmin):
    list_display = ('author','price', 'start_time', 'end_time')
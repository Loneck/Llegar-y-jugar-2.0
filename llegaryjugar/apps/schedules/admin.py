# -*- coding: utf-8 -*-
from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Schedule, SchedulesCreate


@admin.register(Schedule)
class SchedulesAdmin(BaseAdmin):
    list_display = ('court', 'date', 'price', 'start_time', 'end_time',)


@admin.register(SchedulesCreate)
class SchedulesCreateAdmin(BaseAdmin):
    list_display = ('author', 'price', 'start_time', 'end_time',)
    filter_horizontal = ('day', 'month',)

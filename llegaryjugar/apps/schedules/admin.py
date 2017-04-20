from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Schedules

@admin.register(Schedules)
class SchedulesAdmin(BaseAdmin):
    pass
    list_display = ('court','date','start_time','end_time')
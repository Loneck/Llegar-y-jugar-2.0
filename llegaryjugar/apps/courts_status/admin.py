from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import CourtStat


@admin.register(CourtStat)
class CourtStatAdmin(BaseAdmin):
    list_display = ('status',)

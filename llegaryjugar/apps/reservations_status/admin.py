from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import ReservationsStat


@admin.register(ReservationsStat)
class ReservationsStatAdmin(BaseAdmin):
    list_display = ('status',)

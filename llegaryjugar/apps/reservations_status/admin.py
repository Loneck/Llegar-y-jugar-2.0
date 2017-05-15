from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import ReservationsStatus

@admin.register(ReservationsStatus)
class ReservationsStatusAdmin(BaseAdmin):
    pass
    list_display = ('status',)
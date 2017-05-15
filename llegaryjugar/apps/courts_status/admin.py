from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import CourtStatus

@admin.register(CourtStatus)
class CourtStatusAdmin(BaseAdmin):
    pass
    list_display = ('status',)
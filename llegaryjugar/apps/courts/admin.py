from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Court


@admin.register(Court)
class CourtAdmin(BaseAdmin):
    list_display = ('club', 'name', 'number', 'status')

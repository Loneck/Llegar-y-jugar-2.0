from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Service


@admin.register(Service)
class ServiceAdmin(BaseAdmin):
    list_display = ('name', 'price')

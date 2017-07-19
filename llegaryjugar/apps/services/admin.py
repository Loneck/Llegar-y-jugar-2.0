from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Services


@admin.register(Services)
class ServicesAdmin(BaseAdmin):
    list_display = ('name', 'price')

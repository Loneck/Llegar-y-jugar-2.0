from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Courts

@admin.register(Courts)
class CourtsAdmin(BaseAdmin):
    pass
    list_display = ('club', 'name', 'number', 'status')
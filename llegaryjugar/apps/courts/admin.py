from django.contrib import admin
from .models import Courts

@admin.register(Courts)
class CourtsAdmin(BaseAdmin):
    pass
    list_display = ('club','status', 'name', 'number')
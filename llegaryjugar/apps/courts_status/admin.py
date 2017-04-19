from django.contrib import admin
from .models import CourtsStatus

@admin.register(CourtsStatus)
class CourtsStatusAdmin(BaseAdmin):
    pass
    list_display = ('name')
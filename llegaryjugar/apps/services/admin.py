from django.contrib import admin
from .models import Servicesvices

@admin.register(Services)
class ServicesAdmin(BaseAdmin):
    pass
    list_display = ('name','price')
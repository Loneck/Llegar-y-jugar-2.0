from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Clubs


@admin.register(Clubs)
class ClubsAdmin(BaseAdmin):
    list_display = ('name', 'address', 'mail', 'phone_number')

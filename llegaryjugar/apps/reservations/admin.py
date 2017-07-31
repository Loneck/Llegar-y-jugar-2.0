from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from llegaryjugar.apps.reservations.models import Reservation


# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(BaseAdmin):
    list_display = ('client', 'club', 'schedule', 'createdDate', 'price', 'status')

from django.contrib import admin
from .models import Clubs

@admin.register(Clubs)
class ClubsAdmin(BaseAdmin):
    pass
    list_display = ('name','address', 'phone_number')
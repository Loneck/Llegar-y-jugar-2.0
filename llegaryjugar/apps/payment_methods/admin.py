from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import PaymentMethod


@admin.register(PaymentMethod)
class PaymentMethodAdmin(BaseAdmin):
    list_display = ('name', 'status')

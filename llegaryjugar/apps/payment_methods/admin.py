from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import PaymentMethods

@admin.register(PaymentMethods)
class PaymentMethodsAdmin(BaseAdmin):
    list_display = ('name','status')
from django.contrib import admin
from .models import PaymentMethods

@admin.register(PaymentMethods)
class PaymentMethodsAdmin(BaseAdmin):
    pass
    list_display = ('name','status')
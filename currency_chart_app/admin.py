from django.contrib import admin
from .models import CurrencyData

@admin.register(CurrencyData)
class CurrencyDataAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'open', 'high',
                    'low', 'close', 'currency_code']
    list_filter = ['currency_code', 'timestamp']


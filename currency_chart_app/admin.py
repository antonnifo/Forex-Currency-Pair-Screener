from django.contrib import admin

from .models import CurrencyData
from import_export.admin import ImportExportModelAdmin


@admin.register(CurrencyData)
class CurrencyDataAdmin(ImportExportModelAdmin):
    list_display = ['timestamp', 'open', 'high',
                    'low', 'close', 'currency_code']
    list_filter = ['currency_code', 'timestamp']


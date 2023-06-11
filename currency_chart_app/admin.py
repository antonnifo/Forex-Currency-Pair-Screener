from django.contrib import admin

from .models import CurrencyData, Interval
from import_export.admin import ImportExportModelAdmin

@admin.register(Interval)
class IntervalDataAdmin(ImportExportModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]


@admin.register(CurrencyData)
class CurrencyDataAdmin(ImportExportModelAdmin):
    list_display = ['timestamp', 'interval', 'open', 'high',
                    'low', 'close', 'currency_code']
    list_filter = ['currency_code', 'timestamp']


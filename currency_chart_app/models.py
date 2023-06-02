from django.db import models

class CurrencyData(models.Model):
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    currency_code = models.CharField(max_length=10)


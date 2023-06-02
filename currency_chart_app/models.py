from django.db import models

class CurrencyData(models.Model):
    CURRENCY_CHOICES = (
                    ('GBPUSD', 'GBPUSD'),
                    ('EURAUD', 'EURAUD'),
                    ('USDCAD', 'USDCAD'),
                )    

    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    currency_code = models.CharField(max_length=10,choices=CURRENCY_CHOICES, default='USDCAD')

    def __str__(self):
        return self.currency_code
    


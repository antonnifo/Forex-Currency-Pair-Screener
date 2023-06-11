from django.db import models

class Interval(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name    

class CurrencyData(models.Model):
    CURRENCY_CHOICES = (
                    ('GBPUSD', 'GBPUSD'),
                    ('EURAUD', 'EURAUD'),
                    ('USDCAD', 'USDCAD'),
                )    

    interval = models.ForeignKey(Interval, on_delete=models.CASCADE, related_name='interval_data')
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    currency_code = models.CharField(max_length=10,choices=CURRENCY_CHOICES, default='USDCAD')

    def __str__(self):
        return self.currency_code
    

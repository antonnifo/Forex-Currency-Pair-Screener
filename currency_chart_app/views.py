from django.shortcuts import render
import mplfinance as mpf
import pandas as pd
from .models import CurrencyData


def candlestick_chart(request, currency=None):

    currency_data = CurrencyData.objects.filter(currency_code='USDCAD') 
    if currency:
        currency_data = CurrencyData.objects.filter(currency_code=currency) 
    
    data = []
    
    for entry in currency_data:
        data.append({
            'timestamp': entry.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'open': entry.open,
            'high': entry.high,
            'low': entry.low,
            'close': entry.close,
        })
    
    context = {'data': data,
               'currency':currency}

    return render(request, 'currency_chart/candlestick_chart.html', context)
    
from django.shortcuts import render
import mplfinance as mpf
import pandas as pd
from .models import CurrencyData

def candlestick_chart(request):
    # if request.method == 'POST': 
    currency_data = CurrencyData.objects.filter(currency_code='USD') 
    
    data = pd.DataFrame(list(currency_data.values()))

    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)

    context = {'data': data.to_json(orient='records')}
    
    return render(request, 'currency_chart/candlestick_chart.html', context)

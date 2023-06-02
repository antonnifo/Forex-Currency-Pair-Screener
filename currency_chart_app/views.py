from django.shortcuts import render
import mplfinance as mpf
import pandas as pd
from .models import CurrencyData

def candlestick_chart(request, currency=None):

    if currency:
        try:
            currency_data = CurrencyData.objects.filter(currency_code=currency)
        except Exception as e:
            raise Http404('No Currency Data for that Currency Code, Check back later')
    else:
        currency_data = CurrencyData.objects.filter(currency_code='USDCAD')    
    
    print(currency_data)
    data = pd.DataFrame(list(currency_data.values()))

    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)

    context = {'data': data.to_json(orient='records'),
              'currency':currency}
    
    return render(request, 'currency_chart/candlestick_chart.html', context)

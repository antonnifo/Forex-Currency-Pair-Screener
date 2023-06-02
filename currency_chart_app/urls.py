from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [
    path('', views.candlestick_chart, name='home'),
    path('<str:currency>', views.candlestick_chart, name='filter_by_currency'),

]

from currency.use_cases.get_currencies.get_currencies_controller import GetCurrenciesController
from currency.use_cases.get_exchange_rate.get_exchange_rate_controller import GetExchangeRateController
from django.urls import path

urlpatterns = [
    path('exchange-rate', GetExchangeRateController.as_view(), name='currency-exchange-rate'),
    path('', GetCurrenciesController.as_view(), name='currencies-list'),
]
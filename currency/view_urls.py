

from currency.views import CurrencyConverterView
from django.urls import path

urlpatterns = [
    path('currency-converter', CurrencyConverterView.as_view(), name='currency-converter'),
]
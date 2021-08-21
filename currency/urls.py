
from currency.views import CurrencyConverterController
from django.urls import path

urlpatterns = [
    path('converter', CurrencyConverterController.as_view(), name='currency-converter-api'),
]
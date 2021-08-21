from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from currency.models import Currency, Money
from currency.currency_converter.currency_exchange import CurrencyExchange
from currency.currency_converter.currency_converter import CurrencyConverter

# Create your views here.
class CurrencyConverterController(View):
    def get(self, request):
        amount = request.GET['amount']
        from_currency_id = request.GET['from_currency']
        to_currency_id = request.GET['to_currency']

        from_currency = Currency.objects.get(id=from_currency_id)
        to_currency = Currency.objects.get(id=to_currency_id)

        money = Money(float(amount), from_currency)
        exchange_rate = CurrencyExchange().get_exchange_rate(from_currency, to_currency)
        exchanged_money = CurrencyConverter.exchange_money(money, exchange_rate)
        return JsonResponse(exchanged_money.toJson(), status=200)
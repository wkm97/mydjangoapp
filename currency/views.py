from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from currency.models.currency import Currency
from currency.models.money import Money

# Create your views here.
class CurrencyConverterView(View):
    def get(self, request):
        amount = request.GET['amount']
        from_currency_id = request.GET['from_currency']
        to_currency_id = request.GET['to_currency']

        from_currency = Currency.objects.get(id=from_currency_id)
        to_currency = Currency.objects.get(id=to_currency_id)

        money = Money(float(amount), from_currency)
        exchanged_money = money.exchange_currency(to_currency)
        return JsonResponse(exchanged_money.toJson(), status=200)
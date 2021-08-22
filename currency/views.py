from currency.forms import CurrencyConverterForm
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from currency.models.currency import Currency
from currency.models.money import Money

# Create your views here.
class CurrencyConverterView(View):
    template_name = "currency_converter.html"
    def get(self, request):
        context = {}
        form = CurrencyConverterForm()
        
        context['form'] = form
        return render(request, self.template_name, context)
from currency.models.currency import Currency
from typing import Callable, List
from django.http.response import JsonResponse
from dataclasses import dataclass


@dataclass(frozen=True)
class GetCurrenciesResponseDTO:
    currencies: List[Currency]

    def toResponse(self):
        currencies = list(map(lambda x: {"id": x.id, "currency_name": x.currency_name, "currency_symbol": x.currency_symbol}, self.currencies))

        return JsonResponse({"currencies": currencies}, status=200)
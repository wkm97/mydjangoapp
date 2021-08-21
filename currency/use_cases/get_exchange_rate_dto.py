import json
from typing import Callable
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from currency.models.exchange_rate import ExchangeRate
from dataclasses import dataclass

from currency.models.currency import Currency

@dataclass(frozen=True)
class GetExchangeRateRequestDTO:
    from_currency: Currency
    to_currency: Currency


@dataclass(frozen=True)
class GetExchangeRateResponseDTO:
    exchange_rate: ExchangeRate

    def toResponse(self):
        currency_data: Callable[[Currency], dict] = lambda x: { "id": x.id, "currency_name": x.currency_name }
        data = {
            "from_currency": currency_data(self.exchange_rate.from_currency),
            "to_currency": currency_data(self.exchange_rate.to_currency),
            "rate": self.exchange_rate.rate
        }

        return JsonResponse(data, status=200)
        # return {
        #     "from_currency": serializers.serialize('json', self.exchange_rate.from_currency),
        #     "to_currency": self.exchange_rate.to_currency,
        #     "rate": self.exchange_rate.rate
        # }
    
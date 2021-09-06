
from currency.use_cases.get_currencies.get_currencies_dto import GetCurrenciesResponseDTO
from currency.use_cases.get_exchange_rate.get_exchange_rate_dto import GetExchangeRateRequestDTO
from currency.use_cases.get_exchange_rate.get_exchange_rate import GetExchangeRateUseCase
from django.http.response import JsonResponse
from django.views.generic.base import View

from currency.models.currency import Currency



# Create your views here.
class GetCurrenciesController(View):
    def get(self, request):
        try:
            currencies = Currency.objects.all().order_by('id')
            currencies = GetCurrenciesResponseDTO(list(currencies))
            return currencies.toResponse()
        except Exception as e:
            result = {
                "message" : repr(e)
            }
            return JsonResponse(result, status=500)

from currency.use_cases.get_exchange_rate.get_exchange_rate_dto import GetExchangeRateRequestDTO
from currency.use_cases.get_exchange_rate.get_exchange_rate import GetExchangeRateUseCase
from django.http.response import JsonResponse
from django.views.generic.base import View

from currency.models.currency import Currency



# Create your views here.
class GetExchangeRateController(View):
    def get(self, request):
        from_currency_id = request.GET['from_currency']
        to_currency_id = request.GET['to_currency']

        try:
            from_currency = Currency.objects.get(id=from_currency_id)
            to_currency = Currency.objects.get(id=to_currency_id)
            dto = GetExchangeRateRequestDTO(from_currency, to_currency)
            result = GetExchangeRateUseCase.execute(dto)
            return result.toResponse()
        except Exception as e:
            result = {
                "message" : repr(e)
            }
            return JsonResponse(result, status=500)
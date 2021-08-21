
from currency.currency_exchange.currency_exchange_api import CurrencyExchangeAPI
from currency.models.exchange_rate import ExchangeRate, ExchangeRateNotFoundError
from currency.use_cases.get_exchange_rate_dto import GetExchangeRateRequestDTO ,GetExchangeRateResponseDTO


class GetExchangeRateUseCase:
    @staticmethod
    def execute(request: GetExchangeRateRequestDTO) -> GetExchangeRateResponseDTO:
        from_currency = request.from_currency
        to_currency = request.to_currency

        try:
            exchange_rate = ExchangeRate.today.get_exchange_rate(from_currency=from_currency, to_currency=to_currency)
        except ExchangeRateNotFoundError: # If exchange rate not found, request from API
            exchange_rate = CurrencyExchangeAPI().get_exchange_rate(from_currency, to_currency)
            exchange_rate.save()
        
        return GetExchangeRateResponseDTO(exchange_rate)
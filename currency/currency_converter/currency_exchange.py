from currency.currency_converter.currency_exchange_api import CurrencyExchangeAPI
from currency.currency_converter.currency_exchange_interface import CurrencyExchangeInterface
from currency.models import Currency, CurrencyNotAvailableError, ExchangeRate, Money
from django.db.models import QuerySet


class CurrencyExchange(CurrencyExchangeInterface):
    api = CurrencyExchangeAPI() # For fetching data if data not available in database

    def get_available_currencies(self) -> QuerySet[Currency]:
        return Currency.objects.all()
    
    def get_exchange_rate(self, from_currency: Currency, to_currency: Currency) -> ExchangeRate:
        try:
            exchange_rate = ExchangeRate.objects.filter(from_currency=from_currency, to_currency=to_currency).latest('created_at')
            exchange_rate = CurrencyExchange.api.get_exchange_rate(from_currency, to_currency)
        except ExchangeRate.DoesNotExist:
            exchange_rate = CurrencyExchange.api.get_exchange_rate(from_currency, to_currency)
        return exchange_rate





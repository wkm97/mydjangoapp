
from django.db.models.query import QuerySet
from currency.models import Currency, ExchangeRate, Money

class CurrencyExchangeInterface:
    def get_available_currencies(self) -> QuerySet[Currency]:
        pass

    def get_exchange_rate(self, from_currency: Currency, to_currency: Currency) -> ExchangeRate:
        pass
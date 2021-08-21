from currency.models.exchange_rate import ExchangeRate, ExchangeRateNotFoundError
from currency.models.currency import Currency
from django.test import TestCase

from currency.currency_exchange.currency_exchange_api import CurrencyExchangeAPI

class CurrencyExchangeTestCase(TestCase):
    def setUp(self) -> None:
        from_currency = Currency.objects.get(id="USD")
        to_currency = Currency.objects.get(id="MYR")
        ExchangeRate.objects.create(from_currency=from_currency, to_currency=to_currency, rate=4)
    
    def test_get_today_exchange_rate(self):
        ## Success
        from_currency = Currency.objects.get(id="USD")
        to_currency = Currency.objects.get(id="MYR")
        exchange_rate = ExchangeRate.today.get_exchange_rate(from_currency=from_currency, to_currency=to_currency)
        self.assertIsInstance(exchange_rate, ExchangeRate)
        self.assertEqual(exchange_rate.from_currency, from_currency)
        self.assertEqual(exchange_rate.to_currency, to_currency)
        self.assertEqual(exchange_rate.rate, 4)

        ## Invalid Currency
        err_from_currency = Currency(id="098")
        err_to_currency = Currency(id="MYR")
        with self.assertRaises(ExchangeRateNotFoundError):
            exchange_rate = ExchangeRate.today.get_exchange_rate(from_currency=err_from_currency, to_currency=err_to_currency)

        ## Invalid Currency
        err_from_currency = Currency(id="USD")
        err_to_currency = Currency(id="123")
        with self.assertRaises(ExchangeRateNotFoundError):
            exchange_rate = ExchangeRate.today.get_exchange_rate(from_currency=err_from_currency, to_currency=err_to_currency)
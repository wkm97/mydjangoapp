from currency.models import Currency, ExchangeRate, Money
from django.test import TestCase
from currency.currency_converter.currency_exchange_api import CurrencyExchangeAPI, CurrencyNotAvailableError

class CurrencyExchangeAPITestCase(TestCase):
    def setUp(self) -> None:
        CurrencyExchangeAPI().get_available_currencies()
        return super().setUp()

    def test_get_available_currencies(self):
        currencies = CurrencyExchangeAPI().get_available_currencies()
        currencies = list(currencies)
        self.assertGreater(len(currencies), 100, 'Total available currencies more than 100.')
        for currency in currencies:
            self.assertIsInstance(currency, Currency)
    
    def test_get_exchange_rate(self):
        ## Success
        from_currency = Currency.objects.get(id="USD")
        to_currency = Currency.objects.get(id="MYR")
        exchange_rate = CurrencyExchangeAPI().get_exchange_rate(from_currency, to_currency)
        self.assertIsInstance(exchange_rate, ExchangeRate)
        self.assertEqual(exchange_rate.from_currency, from_currency)
        self.assertEqual(exchange_rate.to_currency, to_currency)

        ## Invalid Currency
        err_from_currency = Currency(id="098")
        err_to_currency = Currency(id="MYR")
        with self.assertRaises(CurrencyNotAvailableError):
            exchange_rate = CurrencyExchangeAPI().get_exchange_rate(err_from_currency, err_to_currency)

        ## Invalid Currency
        err_from_currency = Currency(id="USD")
        err_to_currency = Currency(id="123")
        with self.assertRaises(CurrencyNotAvailableError):
            exchange_rate = CurrencyExchangeAPI().get_exchange_rate(err_from_currency, err_to_currency)
            

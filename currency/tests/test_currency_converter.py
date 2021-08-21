
from currency.currency_converter.currency_exchange_api import CurrencyExchangeAPI
from currency.currency_converter.currency_converter import CurrencyConverter
from currency.models import Currency, ExchangeRate, Money
from django.test.testcases import TestCase


class CurrencyConverterTestCase(TestCase):
    def setUp(self) -> None:
        CurrencyExchangeAPI().get_available_currencies()
        return super().setUp()

    def test_exchange_money(self):
        from_currency = Currency(id="USD", currency_name="US Dollar")
        to_currency = Currency(id="MYR", currency_name="Malaysia Ringgit")
        exchange_rate = ExchangeRate(from_currency=from_currency, to_currency=to_currency, rate=4)

        # Success
        input_money = Money(10, from_currency)
        output_money = CurrencyConverter.exchange_money(input_money, exchange_rate)
        self.assertEqual(output_money.currency, to_currency)
        self.assertEqual(output_money.amount, 40)

        # Wrong Input Money
        from_currency = Currency(id="PHP")
        input_money = Money(10, from_currency)
        with self.assertRaises(ValueError):
            output_money = CurrencyConverter.exchange_money(input_money, exchange_rate)
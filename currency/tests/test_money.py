from currency.models.exchange_rate import ExchangeRate, ExchangeRateNotFoundError
from django.test import TestCase
from currency.models.currency import Currency
from currency.models.money import Money

class MoneyTestCase(TestCase):
    def setUp(self) -> None:
        from_currency = Currency.objects.get(id="USD")
        to_currency = Currency.objects.get(id='MYR')
        ExchangeRate.objects.create(from_currency=from_currency, to_currency=to_currency, rate=4)
        self.money = Money(10, from_currency)

    def test_exchange_currency(self):
        # Success
        to_currency = Currency.objects.get(id='MYR')
        new_money = self.money.exchange_currency(to_currency)
        self.assertEqual(40, new_money.amount, '10 USD to 40 MYR')

        # Fail
        to_currency = Currency.objects.get(id='PHP')
        with self.assertRaises(ExchangeRateNotFoundError):
            new_money = self.money.exchange_currency(to_currency)

from currency.models.exchange_rate import ExchangeRate
from currency.models.currency import Currency, CurrencyNotAvailableError


class Money:
    def __init__(self, amount: float, currency: Currency):
        self._check_amount(amount)
        self._check_currency(currency)
        self.amount = amount
        self.currency = currency
    
    def _check_amount(self, amount: float):
        if(amount < 0):
            raise ValueError("Amount must be higher than 1.")
    
    def _check_currency(self, currency: Currency):
        if not Currency.objects.filter(id=currency.id).exists():
            raise CurrencyNotAvailableError("Assigned Currency Is Not Available.")
    
    def exchange_currency(self, to_currency: Currency):
        exchange_rate = ExchangeRate.today.get_exchange_rate(from_currency=self.currency, to_currency=to_currency)
        amount = self.amount * exchange_rate.rate
        money = Money(amount, to_currency)
        return money
    
    def toJson(self):
        return {
            "amount": self.amount,
            "currency": self.currency.id
        }

from currency.models import ExchangeRate, Money


class CurrencyConverter:
    @staticmethod
    def exchange_money(money: Money, exchange_rate: ExchangeRate)->Money:
        if(money.currency != exchange_rate.from_currency):
            raise ValueError("Exchange rate have the different data for from_currency.")
        
        exchanged_amount = money.amount * exchange_rate.rate
        exchanged_money = Money(exchanged_amount, exchange_rate.to_currency)
        return exchanged_money
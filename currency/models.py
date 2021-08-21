from django.core import serializers
from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class CurrencyNotAvailableError(Exception):
    pass

class Currency(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    currency_name = models.CharField(max_length=255, blank=False)
    currency_symbol = models.CharField(max_length=10, blank=True, null=True)

    def toJson(self):
        return {
            "id": self.id,
            "currency_name": self.currency_name,
            "currency_symbol": self.currency_symbol
        }


class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_%(class)s')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_%(class)s')
    rate = models.FloatField(validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)

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
    
    def toJson(self):
        return {
            "amount": self.amount,
            "currency": self.currency.id
        }
        

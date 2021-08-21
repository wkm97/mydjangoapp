from currency.models.currency import Currency
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class ExchangeRateNotFoundError(Exception):
    pass

class TodayManager(models.Manager):
    def get_queryset(self):
        start = timezone.now().replace(hour=0, minute=0, second=0)
        end = timezone.now().replace(hour=23, minute=59, second=59)
        return super().get_queryset().filter(created_at__range=(start, end))
    
    def get_exchange_rate(self, from_currency: Currency, to_currency):
        exchange_rate = self.get_queryset().filter(from_currency=from_currency, to_currency=to_currency).order_by('-created_at').last()
        if exchange_rate is None:
            raise ExchangeRateNotFoundError("Exchange rate not found in database.")
        return exchange_rate
        

class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_%(class)s')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_%(class)s')
    rate = models.FloatField(validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    today = TodayManager()

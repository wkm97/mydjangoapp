from django.db import models

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
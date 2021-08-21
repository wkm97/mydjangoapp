from typing import List
from django.conf import settings

import requests

from currency.models.currency import Currency, CurrencyNotAvailableError
from currency.models.exchange_rate import ExchangeRate

class APIClientError(Exception):
    pass

# Store data to database
class CurrencyExchangeAPI:
    url = "https://free.currconv.com"
    params = {
        "apiKey": settings.FREE_CURRCONV_API_KEY
    }

    def get_available_currencies(self) -> List[Currency]:
        currencies = []
        url = CurrencyExchangeAPI.url + "/api/v7/currencies"
        params = CurrencyExchangeAPI.params

        response = requests.get(url, params=params)
        if(response.status_code == 200):
            results = response.json()['results']
            for result in results.values():
                id = result['id']
                currency_name = result['currencyName']
                currency_symbol = result['currencySymbol'] if 'currencySymbol' in result.keys() else None
                currency = Currency(id=id, currency_name=currency_name, currency_symbol=currency_symbol)
                currencies.append(currency)
        else:
            raise APIClientError("Failed to Fetch result", response.json())
        
        return currencies
    
    def get_exchange_rate(self, from_currency: Currency, to_currency: Currency) -> ExchangeRate:
        url = CurrencyExchangeAPI.url + "/api/v7/convert"

        from_id = from_currency.id
        to_id = to_currency.id

        # IF Currency not available in database, return error.
        if not Currency.objects.filter(id=from_id).exists():
            raise CurrencyNotAvailableError("From Currency Not Available.")
        if not Currency.objects.filter(id=to_id).exists():
            raise CurrencyNotAvailableError("To Currency Not Available.")
            
        query = "{}_{}".format(from_id, to_id) 
        params = {
            **CurrencyExchangeAPI.params,
            "q": query,
            "compact":"ultra", # Shorter response result 
        }

        response = requests.get(url, params)
        if(response.status_code == 200):
            results = response.json()
            rate = results[query]
            exchange_rate = ExchangeRate(from_currency=from_currency, to_currency=to_currency, rate=rate)
        else:
            raise APIClientError(response.json())

        return exchange_rate
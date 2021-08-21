
import requests
from django.conf import settings
from currency.models import Currency, CurrencyNotAvailableError, ExchangeRate, Money
from currency.currency_converter.currency_exchange_interface import CurrencyExchangeInterface


class APIClientError(Exception):
    pass

# Store data to database
class CurrencyExchangeAPI(CurrencyExchangeInterface):
    url = "https://free.currconv.com"
    params = {
        "apiKey": settings.FREE_CURRCONV_API_KEY
    }

    def get_available_currencies(self):
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
                Currency.objects.update_or_create(id=id, currency_name=currency_name, currency_symbol=currency_symbol)
        else:
            raise APIClientError("Failed to Fetch result")
        currencies = Currency.objects.all()
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
            
        query = "{}_{},{}_{}".format(from_id, to_id, to_id, from_id) # Get both way of conversion, Example: USD_MYR,MYR_USD 
        params = {
            **CurrencyExchangeAPI.params,
            "q": query,
            "compact":"ultra", # Shorter response result 
        }

        # Store Both Way Conversion Rate to database
        response = requests.get(url, params)
        if(response.status_code == 200):
            results = response.json()
            for key, value in results.items():
                tmp_from_id, tmp_to_id = key.split("_")
                rate = value
                tmp_from_currency = Currency.objects.get(id=tmp_from_id)
                tmp_to_currency = Currency.objects.get(id=tmp_to_id)
                ExchangeRate.objects.create(from_currency=tmp_from_currency, to_currency=tmp_to_currency, rate=rate)
        else:
            raise APIClientError(response.json())

        exchange_rate = ExchangeRate.objects.filter(from_currency=from_currency, to_currency=to_currency).latest('created_at')
        return exchange_rate
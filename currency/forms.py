from currency.models.currency import Currency
from django import forms
from django.core import validators
from django.core.validators import *
from django.db.utils import ProgrammingError

class CurrencyConverterForm(forms.Form):
    try:
        CURRENCIES_CHOICES = tuple(Currency.objects.all().values_list('id', 'currency_name').order_by('id'))
    except ProgrammingError:
        CURRENCIES_CHOICES = (('USD', 'US Dollar'), ('MYR', 'Malaysia Ringgit'))
    amount = forms.DecimalField(
        min_value=1, 
        decimal_places=2, 
        label="Amount", 
        label_suffix="",
        widget = forms.NumberInput(attrs = {'value':"1"})
        )
    from_currency_id = forms.ChoiceField(choices=CURRENCIES_CHOICES, initial=CURRENCIES_CHOICES[0])
    to_currency_id = forms.ChoiceField(
        choices=CURRENCIES_CHOICES, 
        initial=CURRENCIES_CHOICES[9],
        widget = forms.Select(attrs = {'class':"to-currency"})
    )
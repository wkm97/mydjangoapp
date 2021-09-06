from currency.models.currency import Currency
from django import forms
from django.core.validators import *

class CurrencyConverterForm(forms.Form):
    amount = forms.DecimalField(
        min_value=1, 
        decimal_places=2, 
        label="Amount", 
        label_suffix="",
        widget = forms.NumberInput(attrs = {'value':"1"})
        )
    from_currency_id = forms.ChoiceField()
    to_currency_id = forms.ChoiceField(
        widget = forms.Select(attrs = {'class':"to-currency"})
    )
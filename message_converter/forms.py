from django import forms

class MessageConverterForm(forms.Form):
    input = forms.CharField(required=False)
    output = forms.CharField(disabled=True, required=False)
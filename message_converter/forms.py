from django import forms

class MessageConverterForm(forms.Form):
    input = forms.CharField(required=False, label_suffix="", label="Original message")
    output = forms.CharField(disabled=True, required=False, label_suffix="", label="Message in Lowercase")
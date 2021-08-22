from django import forms

class MessageConverterForm(forms.Form):
    input = forms.CharField(
        required=False, 
        label_suffix="", 
        label="Original message",
        widget=forms.TextInput(attrs={'placeholder': 'Input Box'})
    )
    output = forms.CharField(
        disabled=True, 
        required=False, 
        label_suffix="", 
        label="Message in Lowercase",
        widget=forms.TextInput(attrs={'placeholder': 'Display entered message in lowercase'})
    )
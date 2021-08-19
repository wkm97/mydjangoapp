from django.shortcuts import render
from django.views import View
from message_converter.string_utils import convert_to_lowercase
from message_converter.forms import MessageConverterForm

# Create your views here.
class MessageConverterView(View):
    template_name = 'message_converter.html'

    def get(self, request):
        context = {}
        form = MessageConverterForm(request.GET)
        if form.is_valid():
            input = form.cleaned_data['input']
            output = convert_to_lowercase(input)
            form = MessageConverterForm(initial={'input': input, 'output': output})

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


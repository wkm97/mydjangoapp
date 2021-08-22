from django.views import View
from django.shortcuts import render

class HomepageView(View):
    template_name = 'homepage.html'

    def get(self, request):
        return render(request, self.template_name, {})
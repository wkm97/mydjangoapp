from django.urls import path
from message_converter.views import MessageConverterView

urlpatterns = [
    path('message-converter/', MessageConverterView.as_view(), name='message-converter'),
]
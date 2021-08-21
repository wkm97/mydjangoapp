from django.test import TestCase
from message_converter.string_utils import convert_to_lowercase
# Create your tests here.
class MessageConverterTestCase(TestCase):
    
    def test_to_lowercase(self) -> None:
        result = convert_to_lowercase("HELLO WORLD")
        self.assertEqual(result, 'hello world')
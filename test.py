from app import app
from unittest import TestCase

# app.config['TESTING'] = True
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar'] 

class ConversionTestCase(TestCase):
    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<h1 class="text-center text-primary bg-info p-3">FOREX CONVERTER</h1>',html)
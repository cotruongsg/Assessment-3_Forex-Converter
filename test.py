from app import app
from unittest import TestCase

# app.config['TESTING'] = True
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar'] 

class ConversionTestCase(TestCase):
    # Test if Route is loaded correctly
    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<h1 class="text-center text-primary bg-info p-3">FOREX CONVERTER</h1>',html)

    # Test Valid Input and Direct to Result page
    def test_valid_input(self):
        with app.test_client() as client:
            res = client.post('/currencyconversion',data={'from_currency':'USD','to_currency':'EUR','amount':100})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<p>The result is €91.06</p>', html)

    # Test Invalid input and Redirect to mainpage with wrong input stills loaded
    def test_invalid_input(self):
        with app.test_client() as client:
            res = client.post('/currencyconversion',data={'from_currency':'AAA','to_currency':'EUR','amount':100})
            self.assertEqual(res.status_code,302)

    
           


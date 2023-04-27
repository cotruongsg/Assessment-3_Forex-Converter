from decimal import Decimal 
from flask import Flask , flash , render_template , request , redirect ,url_for , session
from flask_debugtoolbar import DebugToolbarExtension
import requests
from forex_python.converter import CurrencyCodes 


app = Flask(__name__)
app.config['SECRET_KEY'] = "helloWorld"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def homepage():
    return render_template("currency_converter_mainpage.html")
    

@app.route('/currencyconversion', methods=['POST'])
def currency_converter():   
    code = CurrencyCodes()
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = request.form['amount']

    # Validate Currency
    if not code.get_symbol(from_currency):
        flash(f"Invalid currency code {from_currency}",'error')
    
    if not code.get_symbol(to_currency):
        flash(f"Invalid currency code {to_currency}",'error')

    # Check if amount is not empty and is a positive number
    # Convert it to a float and check if it is less than or equal to 0.
    amount = Decimal(request.form["amount"])    
    if amount <= 0 :
        flash("Invalid Amount . Please enter a positive number and greater than 0.",'error')
   
    # Store the form data in the session
    session['from_currency'] = from_currency
    session['to_currency'] = to_currency
    session['amount'] = amount

    if code.get_symbol(from_currency) and code.get_symbol(to_currency) and amount > 0 :
        # Convert into Symbol       
        symbol = code.get_symbol(to_currency)

        # API_URL to convert currency
        api_url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}'
        response = requests.get(api_url)         
        conversion_result = round(response.json()['result'],2)            
        return render_template('result.html', symbol=symbol, result=conversion_result)
    else:        
        return redirect('/mainpage')
    
# If input is valid , the page will redirect to homepage but keeping the wrong information on screen    
@app.route('/mainpage')
def returnToMainPage():
    # The reason None is used as the default value in session.pop('from_currency', '') is to avoid raising a KeyError if the 'from_currency' key does not exist in the session dictionary.
    # If the key does not exist, the pop() method will simply return '' instead of raising an error. 
    # This can be useful when you want to remove an item from the session dictionary, but you're not sure if the item actually exists.
    from_currency = session.pop('from_currency', '')
    to_currency = session.pop('to_currency', '')
    amount = session.pop('amount', '')
    return render_template("currency_converter_mainpage.html", from_currency=from_currency, to_currency=to_currency, amount=amount)

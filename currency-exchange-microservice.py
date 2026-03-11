"""
The Currency Exchange Rate Microservice.
Written in Python and using FLASK REST API.
It accepts floats in USD and converts that value into
a designated country's currency. Returns a float.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# give each country a code
country_currency_map = {
    "France": "EUR",
    "Japan": "JPY",
    "India": "INR",
    "Canada": "CAD",
    "United Kingdom": "GBP",
    "Australia": "AUD"
}

# hard coded exchange rates from USD to the
# supported countries
exchange_rates = {
    "EUR": 0.92,   # Euro
    "JPY": 150.10, # Japanese Yen
    "INR": 83.20,  # Indian Rupee
    "CAD": 1.36,   # Canadian Dollar
    "GBP": 0.78,   # British Pound
    "AUD": 1.52    # Australian Dollar
}

@app.route('/convert', methods=['POST'])
def convert_currency():
    """
    takes a json file that has an accepted country
    and a dollar amount in USD. performs conversion
    in the chosen country's currency.
    :return: the original amount, the converted amount,
    and the currency code
    """
    data = request.get_json()
    usd_amount = data.get("amount")
    country = data.get("country").title()

    if usd_amount is None or country is None:
        return jsonify({"error": "Please provide 'amount' and 'country'"}), 400

    # get currency code and exchange rate
    # perform the math to convert money
    currency_code = country_currency_map.get(country)
    rate = exchange_rates.get(currency_code)
    converted_amount = usd_amount * rate

    return jsonify({
        "usd_amount": usd_amount,
        "converted_amount": round(converted_amount, 2),
        "currency": currency_code
    })

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("Currency Exchange Rate Microservice is Running")
    print("http://localhost:5002")
    print("=" * 50 + "\n")

    app.run(host='localhost', port=5002, debug=True)

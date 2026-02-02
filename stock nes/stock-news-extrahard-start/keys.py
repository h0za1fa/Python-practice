STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import os

ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_KEY')
ALPHAVANTAGE_ENDPOINT_URL = "https://www.alphavantage.co/query?"
ALPHAVANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY,
}

NEWSAPIKEY = os.getenv('NEWSAPI_KEY')
NEWSAPI_ENDPOINT_URL = "https://newsapi.org/v2/everything"
NEWSAPI_PARAMS = {
    'q': 'Tesla',
    'apiKey': NEWSAPIKEY,
}

from_twillio = os.getenv('TWILIO_NUMBER')
to_twillio = os.getenv('PHONE_NUMBER')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
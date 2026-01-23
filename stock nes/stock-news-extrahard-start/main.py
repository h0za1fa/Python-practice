import requests
import datetime
import tesladata
from twilio.rest import Client
from keys import *

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


date_today = datetime.date.today()
# print(str(date_today))
date_yesterday = date_today - datetime.timedelta(days=1)
# print(str(date_yesterday))
date_day_before_yesterday = date_today - datetime.timedelta(days=2)

# response_stock = requests.get(ALPHAVANTAGE_ENDPOINT_URL, params=ALPHAVANTAGE_PARAMS)
# stock_data = response_stock.json()

stock_data = tesladata.tesla_data # remove when using api

# print(stock_data)

closing_yesterday = float(stock_data["Time Series (Daily)"][str(date_yesterday)]['4. close' ])
closing_day_before_yesterday = float(stock_data["Time Series (Daily)"][str(date_day_before_yesterday)]['4. close' ])

variance_perc = ((closing_day_before_yesterday - closing_yesterday) / closing_yesterday) * 100
print(variance_perc)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_response = requests.get(NEWSAPI_ENDPOINT_URL, params=NEWSAPI_PARAMS)
news_articles = news_response.json()

headline = news_articles["articles"][0]["title"]
brief = news_articles["articles"][0]["description"]

print(headline)
print(brief)

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

if variance_perc > 0:
    emoji = '🔺'
else:
    emoji = '🔻'


client = Client(account_sid, auth_token)

message = client.messages.create(
    body= f'TSLA {emoji}{(int(variance_perc))}\nBrief: {brief}',
    from_=from_twillio,
    to=to_twillio,
)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


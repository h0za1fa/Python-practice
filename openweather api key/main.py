import requests
import os
from twilio.rest import Client



key = ''
lat = 30.197838
lon = 71.4719683

endpoint = 'https://api.openweathermap.org/data/2.5/forecast?'

params = {
    'lat': lat,
    'lon': lon,
    'appid': key,
    'cnt': 4
}

response = requests.get(endpoint, params=params)
response.raise_for_status()

res = response.json()

bring_umbrella = False

for step in range(4):
    weather_id = res['list'][step]['weather'][0]['id']

    if weather_id < 800:
        bring_umbrella = True
        break

if bring_umbrella:
    status = 'Bring your shelter'
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= status,
        from_="+",
        to="+",
    )

    print('sent message')
    print(message.sid)

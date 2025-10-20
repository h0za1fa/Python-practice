import requests

# response = requests.get(url='http://api.open-notify.org/iss-now.json')

# response.raise_for_status()

# data = response.json()['iss_position']

# print(data)

parameters = {
		'lat': 40.519066,
		'lng': 40.519066,
		'formatted': 0,	
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters )
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunset)
import requests
import warnings

# Silencing the SSL warning for your Python 3.14 environment
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

TOKEN = 'hueunf8435jj2583225'
USERNAME = 'hozaifa'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Creating the user with verify=False to bypass your local SSL handshake error
response = requests.post(url=PIXELA_ENDPOINT, json=user_params, verify=False)

print(response.text)
import requests
from aiohttp.helpers import TOKEN

TOKEN = 'hueunf8435jj2583225'
USERNAME = 'hozaifa'

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
params_user = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

POST_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
params_graph = {
    'id': 'graph1',
    'name': USERNAME,
    'unit': 'moshs',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=PIXELA_ENDPOINT, json=params_user)

response = requests.post(url=POST_ENDPOINT, json=params_graph, headers=headers,verify=False)

print(response.text)

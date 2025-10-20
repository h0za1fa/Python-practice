import requests
question_api = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
question_api.raise_for_status()
question_data = question_api.json()['results']
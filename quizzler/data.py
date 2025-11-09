import requests as rq

question_data = []

file = rq.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
question_data = file.json()['results']
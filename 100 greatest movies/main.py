from bs4 import BeautifulSoup
from curl_cffi import requests

nums = [str(num) for num in range(1,101)]

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/', impersonate="chrome110")
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.select('h2 strong')

title_list = [title.text for title in titles  if title.text.split(")")[0] in nums ]
title_list.reverse()

with open('titles.txt', 'w') as f:
    for title in title_list:
        f.write(title + '\n')
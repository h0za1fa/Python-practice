from bs4 import BeautifulSoup
import requests

# with open("website.html", "r", encoding="UTF-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

response = requests.get('https://news.ycombinator.com/')


yc_news = BeautifulSoup(response.content, 'html.parser')


titles = yc_news.find_all('span', class_='titleline')
votes = yc_news.find_all('span', class_='score')

# for (title,vote) in zip(titles,votes):
#     print(title.text)
#     print(title.a['href'])
#     print(vote.text)

titles_text_list = [title.text for title in titles]
titles_links_list = [title.a['href'] for title in titles]
titles_votes_list = [int(vote.text.split(' ')[0] )for vote in votes]

max_votes = max(titles_votes_list)
max_votes_index = titles_votes_list.index(max_votes)

print(titles_text_list[max_votes_index])
print(titles_links_list[max_votes_index])
print(max_votes)


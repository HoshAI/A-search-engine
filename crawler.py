import requests
from bs4 import BeautifulSoup

start_url = 'https://stackoverflow.com/questions/'

response = requests.get(start_url)
content = BeautifulSoup(response.text, 'lxml')
links = content.findAll('a', {'class': 'question-hyperlink'})

for link in links:
  print(link['href'], link.text)

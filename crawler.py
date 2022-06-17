import requests
from bs4 import BeautifulSoup

start_url = 'https://stackoverflow.com/questions/?tab=newest&pagesize=50'

response = requests.get(start_url)
content = BeautifulSoup(response.text, 'lxml')
links = content.findAll('a', {'class': 'question-hyperlink'})

for link in links:
  if 'https://' not in link['href']:
  print(link['href'])

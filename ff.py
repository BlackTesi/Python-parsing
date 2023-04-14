import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()
date_str = now.strftime('%Y-%m-%d')
url = 'https://pythonru.com/news/{date_str}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.find_all('div', class_='td-block-row')

for row in rows:
    title = row.find('h3', class_='entry-title td-module-title').text
    link = row.find('a')['href']
    print(title)
    print(link)
    print('--------------------')
import requests
from bs4 import BeautifulSoup


url = "https://24.kg/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
news_titles = soup.find_all('div', class_='one')

for title in news_titles:
    print(title.text)
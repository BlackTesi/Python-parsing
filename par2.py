import requests
from bs4 import BeautifulSoup


url = "https://finewords.ru/cit/citaty-velikix-lyudej"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.find_all('div', class_='cit')

for title in titles:
    print(title.text)
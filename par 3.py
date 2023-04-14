import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.roblox.com/games")
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", class_='games-list')

for row in table.find_all("tr")[1:]:
    name = row.find("a", class_='game-name').text.strip()
    visitors = row.find("td", class_='visits').text.strip()

    print(f"{name}: {visitors} посетителей за последние 24 часа")
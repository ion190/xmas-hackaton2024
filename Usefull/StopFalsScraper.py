import requests
from bs4 import BeautifulSoup

url = 'https://stopfals.md/ro/article/activitate-concertata-pe-telegram-o-retea-de-canale-dedicate-comunitatilor-locale-raspandeste-naratiuni-false-rusesti-si-il-promoveaza-pe-sor-181070'  # Adresa URL a paginii din care extragem date

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Găsirea posturilor din div-ul cu ID-ul "latest-falses"
posts = soup.find('div', {'id': 'latest-falses'}).find_all('div', class_='post post--xxs', limit=6)

for post in posts:
    date = post.find('span', class_='date').text.strip()
    title = post.find('a', class_='title').text.strip()
    views = post.find('span', class_='views').text.strip()
    link = post.find('a', class_='title')['href']

    print(f"Title: {title}")
    print(f"Date: {date}")
    print(f"Views: {views}")
    print(f"Link: {link}\n")

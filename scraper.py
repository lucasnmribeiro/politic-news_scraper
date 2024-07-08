import requests
from bs4 import BeautifulSoup

def scrape_g1():
    url = "https://g1.globo.com/politica/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for item in soup.find_all('div', class_='feed-post-body'):
        title_tag = item.find('a', class_='feed-post-link')
        if title_tag:
            title = title_tag.get_text().strip()
            link = title_tag['href']
            articles.append({'title': title, 'link': link})

    return articles
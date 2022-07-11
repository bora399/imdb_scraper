import time
from bs4 import BeautifulSoup as bs
import requests

source = requests.get("https://www.imdb.com/list/ls070233852/")
soup = bs(source.content, 'html.parser')
movies = []
for baslik in soup.find_all("div", class_="lister-item-content"):
    movie_title = baslik.find("h3", class_="lister-item-header")
    movie_id = baslik.find("h3", class_="lister-item-header").find('a').get('href').split('/')[2]
    movie_year = ''.join(c for c in baslik.find("span", class_="lister-item-year").getText(strip=True) if c.isdigit())
    movie_rating = baslik.find("span", class_="ipl-rating-star__rating").getText(strip=True)
    movie_runtime = baslik.find("span", class_="runtime").getText(strip=True)
    movie_description = baslik.find("p").findNext("p").getText(strip=True)
    movie = {
        'movie_id': baslik.find("h3", class_="lister-item-header").find('a').get('href').split('/')[2],
        'movie_title': baslik.find("h3", class_="lister-item-header").find('a').getText(strip=True),
        'movie_year': ''.join(c for c in baslik.find("span", class_="lister-item-year").getText(strip=True) if c.isdigit()),
        'movie_rating': baslik.find("span", class_="ipl-rating-star__rating").getText(strip=True),
        'movie_runtime': baslik.find("span", class_="runtime").getText(strip=True),
        'movie_description': baslik.find("p").findNext("p").getText(strip=True)
    }
    movies.append(movie)
    #print(movie)

print(movies)
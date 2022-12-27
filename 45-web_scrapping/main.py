from bs4 import BeautifulSoup as bs
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
re = response.text
'''
soup = bs(re, 'html.parser')
a = soup.find(name="a", class_="titlelink")
print(a.getText())
print(a.get('href'))
'''

soup = bs(re, 'html.parser')
all_title = soup.find_all(name='h3', class_='title')
data_movies = [y.getText() for y in all_title]
print(data_movies)
data_movies = list(reversed(data_movies))


for x in data_movies:
    with open('file.txt', 'a', encoding="utf-8") as file:
        file.write("{}\n".format(str(x)))
        file.close()


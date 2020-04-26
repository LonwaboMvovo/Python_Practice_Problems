# https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
import requests
from bs4 import BeautifulSoup as BS

monica_lewinsky_humiliation_culture_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(monica_lewinsky_humiliation_culture_url)
soup = BS(r.text, features='html.parser')

for line in soup.find_all(class_ = 'grid--item body body__container article__body grid-layout__content'):
    if line.p: print(f'\n{line.p.text}')
    else: print(line.contents[0])
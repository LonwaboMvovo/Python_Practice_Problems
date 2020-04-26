# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
import requests
from bs4 import BeautifulSoup

ny_times_url = 'https://www.nytimes.com/'
r = requests.get(ny_times_url)
soup = BeautifulSoup(r.text, features='html.parser')

for story_heading in soup.find_all(class_ = 'css-1ez5fsm'):
    try: print(f'\n{story_heading.h2.text.strip()}')
    except: print("Couldn't find what your looking for")
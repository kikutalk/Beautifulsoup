import requests
from bs4 import BeautifulSoup

res = requests.get('https://yahoo.co.jp')
soup = BeautifulSoup(res.content, 'html.parser')

for a in soup.select('a.entry-link'):
    print(a['href'], a.text)

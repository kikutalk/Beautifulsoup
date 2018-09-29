import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.yahoo.co.jp/flash')
soup = BeautifulSoup(response.text,'lxml')
links = soup.findAll('a')
for link in links:
   print(link.get('href'))

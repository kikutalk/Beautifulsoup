import requests
from bs4 import BeautifulSoup



response = requests.get('https://news.yahoo.co.jp/topics')
url = 'http://news.yahoo.co.jp/topics'
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")


lis = soup.find_all("li",class_="ttl")  # 全ての<h1 class="ttl">...</h1>を取得
for li in lis:
    print(li.text)
ps = soup.find_all("p",class_="ttl")  # 全ての<p class="ttl">...</p>を取得
for p in ps:
    print(p.text)

for a in soup.find_all('a'):
    print(a.text)

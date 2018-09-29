import requests
url = "https://news.yahoo.co.jp/topics"
r = requests.get(url)
print(r.text)

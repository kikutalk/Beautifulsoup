import requests
from bs4 import BeautifulSoup



response = requests.get('https://news.yahoo.co.jp/topics')
bs = BeautifulSoup(response.text,'lxml')


news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

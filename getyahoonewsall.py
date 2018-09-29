from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/Users/kikutalk/Desktop/Beautifulsoup/chromedriver.exe")
#webdriver.Chromeに渡しているのは先ほどダウンロードしたchrome driverのpathです。

#そして本題、いよいよニュース記事の取得に入っていこうかと思います。

def get_yahoonews():
        driver.get("http://news.yahoo.co.jp/list/?c=world")
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        for list in soup.body.find("ul", class_="list").find_all("li"):
            category = list.find("span", class_="cate").string
            title = list.find("span", class_="ttl").string
            href = list.a.get("href")

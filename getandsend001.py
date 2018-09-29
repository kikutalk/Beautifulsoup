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



import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = 'kikutalk@gmail.com'
MY_PASSWORD = 'mbi03JUL!!!'
TO_ADDRESS = 'yoyoginosakura@gmail.com'
BCC = 'figarojp@gmail.com'
SUBJECT = 'GetAndtestの送信テストです。菊'
BODY = fin=open('yokoyoko.txt')
line=fin.read()
print(line)
fin.close()


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg)

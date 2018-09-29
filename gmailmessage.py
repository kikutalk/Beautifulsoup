import smtplib
from email.message import EmailMessage
from datetime import datetime

with open( "yokoyoko.txt" ) as file:   # さっきのログファイルを指定して読み込み
	msg = EmailMessage()
	msg.set_content(file.read())

msg["Subject"] = "BOT稼働状況の通知：{}".format(datetime.now().strftime("%Y-%m-%d-%H-%M"))
msg["From"] = "kikutalk@gmail.com"         # 送信元のアドレス
msg["To"] = "yoyoginosakura@gmail.com"           # 受け取りたいアドレス

server = smtplib.SMTP("smtp.gmail.com",587)    # これはGmailのSMTPなら共通
server.starttls()
server.login("kikutalk@gmail.com", "mbi03JUL!!!")            # Gmailのアカウント名とパスワード
server.sendmail( msg["From"],msg["To"],msg.as_string() )
server.close()

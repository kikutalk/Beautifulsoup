#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import datetime
import smtplib

from email import Encoders
from email.Utils import formatdate
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def create_message(from_addr, to_addr, subject, body, mime, attach_file):
    """
    Mailのメッセージを構築する
    """
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()

    body = MIMEText(body)
    msg.attach(body)

    # 添付ファイルのMIMEタイプを指定する
    attachment = MIMEBase(mime['type'],mime['subtype'])
    # 添付ファイルのデータをセットする
    file = open(attach_file['path'])
    attachment.set_payload(file.read())
    file.close()
    Encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header("Content-Disposition","attachment", filename=attach_file['name'])

    return msg


def send(from_addr, to_addrs, msg):
    """
    Mailを送信する
    """
    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.close()


if __name__ == '__main__':
    from_addr = "kikutalk@gmail.com"
    to_addr = "yoyoginosakura@gmail.com"
    subject = "ファイル添付"
    body = "test body"
    #ここ追加
    mime={'type':'text', 'subtype':'comma-separated-values'}
    #ここも追加
    attach_file={'name':'test.csv', 'path':'/tmp/test.csv'}
    msg = create_message(from_addr, to_addr, subject, body, mime, attach_file)
    send(from_addr, [to_addr], msg)

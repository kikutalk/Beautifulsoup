import sendgrid
from sendgrid.helpers.mail import *
import base64

SG_API_KEY = 'xxxxxxxxxxxxxxxxxx'

sg = sendgrid.SendGridAPIClient(apikey=SG_API_KEY)


from_email = Email('kikutalk@gmail.com')
to_email = Email('yoyoginosakura@gmail.com')
subject = 'test'
body = 'testtesttest'
content = Content('text/plain', body)

mail = Mail(from_email, subject, to_email, content)

with open('C:/Users/kikutalk/Desktop/Beautifulsoup/yokoyoko.txt', 'rb') as f:
   data = f.read()
   f.close()
encoded = base64.b64encode(data)

attachment = Attachment()
attachment.set_content(encoded)
attachment.set_type('application/pdf')
attachment.set_filename('yokoyoko.txt')
attachment.set_disposition('attachment')

mail.add_attachment(attachment)

response = sg.client.mail.send.post(request_body=mail.get())

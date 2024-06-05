import smtplib
import ssl
from email.message import EmailMessage

subject = 'message subject'
body = 'message body'
sender_email = 'sender'
receiver_email = 'receiver'
password = input('Enter password: ')

message = EmailMessage()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

print('Sending...')
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Success')

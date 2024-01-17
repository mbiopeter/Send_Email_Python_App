#Go over to your Gmail account and setup 2 factor authentication
#generate app password
#create a function to send the email
import os
from email.message import EmailMessage

email_sender = 'mbiopeter401@gmail.com'
email_password = os.environ.get('APP_PASSWORD')

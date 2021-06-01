import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from helpers.page import Page

import helpers.config as config

def send(page_config: Page, msg_body: str):
    msg = MIMEMultipart() 

    msg['From'] = config.from_email
    msg['To'] = page_config.to_email

    msg['Subject'] = page_config.mail_subject
    msg.attach(MIMEText(msg_body, 'plain')) 

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 

    s.login(msg['From'], config.gmail_api_key) 

    text = msg.as_string() 

    s.sendmail(msg['From'], msg['From'], text)
    s.quit()

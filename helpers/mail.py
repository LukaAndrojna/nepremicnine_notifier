import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from helpers.page import Page

class Mail:
    def __init__(self):
        pass
    
    def set_parameters_listings(self, page_config: Page, msg_body: str):
        self.from_email = page_config.from_email
        self.gmail_api_key = page_config.gmail_api_key
        self.to_email = list(page_config.to_email) if isinstance(page_config.to_email, str) else page_config.to_email
        self.mail_subject = page_config.mail_subject
        self.msg_body = msg_body
        
        return self
    
    def set_parameters_error(self, from_email: str, gmail_api_key: str, to_email: list, mail_subject: str, msg_body: str):
        self.from_email = from_email
        self.gmail_api_key = gmail_api_key
        self.to_email = list(to_email) if isinstance(to_email, str) else to_email
        self.mail_subject = mail_subject
        self.msg_body = msg_body

        return self
    
    def send(self) -> None:
        msg = MIMEMultipart() 

        msg['From'] = self.from_email
        msg['To'] = ', '.join(self.to_email)

        msg['Subject'] = self.mail_subject
        msg.attach(MIMEText(self.msg_body, 'plain')) 

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls() 

        s.login(msg['From'], self.gmail_api_key) 

        text = msg.as_string() 
        
        s.sendmail(msg['From'], self.to_email, text)
        s.quit()

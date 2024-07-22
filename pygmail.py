import os
from email.message import EmailMessage
import ssl
import smtplib
import re
import time

class Mail:
    def __init__(self, sender = None, password = None, receiver = None, subject = None, body = None):

        self._sender = sender
        self._receiver = receiver
        self._subject = subject
        self._password = password
        self._body = body
        self._context = ssl.create_default_context()
        self._em = EmailMessage()

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, s):
        self._sender = s

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, r):
        self._receiver = r

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, s):
        self._subject = s

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pw):
        self._password = pw

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, b):
        self._body = b

    def send(self):
        if self.sender and self.receiver and self.subject and self.body:
            self._em['From'] = self.sender
            self._em['To'] = self.receiver
            self._em['Subject'] = self.subject
            self._em.set_content(self.body)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = self._context) as smtp:
                smtp.login(self.sender, self.password)
                smtp.sendmail(self.sender, self.receiver, self._em.as_string())
        else:
            print("Please provide details")
            exit(0)

    def sendafter(self, t: str):
        if t:
            m = re.match(r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?', t)
            
            if m:
                h, m, s = m.groups(default=0)
                h = int(h)
                m = int(m)
                s = int(s)
                time.sleep(h * 3600 + m * 60 + s)
                self.send()

        else:
            print("Time format should be in hh:mm:ss")



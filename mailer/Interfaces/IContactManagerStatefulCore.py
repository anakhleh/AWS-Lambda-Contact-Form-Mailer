#IContactManagerStatefulCore.py

import abc
from imaplib import IMAP4_SSL
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailer.DTOs import ContactFormDTO

class IContactManagerStatefulCore(abc.ABC):

    @abc.abstractmethod
    def getAuthenticatedSmtpServer(self) -> SMTP_SSL:
        pass

    @abc.abstractmethod
    def DisconnectSmtpServerAndReturnTrueOnSuccessFalseOnFail(self, smtpServer: SMTP_SSL) -> None:
        pass
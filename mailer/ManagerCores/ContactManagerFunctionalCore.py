#ContactManagerFunctionalCore.py

import re
from mailer.Interfaces import IContactManagerFunctionalCore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailer.DTOs import ContactFormDTO

class ContactManagerFunctionalCore(IContactManagerFunctionalCore):

    def userEmailUserGivenNameUserMessageAreAllPresentAndAreStrings(self, contactFormDTO: ContactFormDTO = None) -> bool:
        if contactFormDTO == None:
            raise ValueError("ContactFormDTO cannot be None.")

        return (isinstance(contactFormDTO.userMessage, str)
                and contactFormDTO.userMessage != ''
                and not contactFormDTO.userMessage.isspace())\
            and (isinstance(contactFormDTO.userGivenName, str)
                and contactFormDTO.userGivenName != ''
                and not contactFormDTO.userGivenName.isspace()) \
            and (isinstance(contactFormDTO.userEmail, str)
                and contactFormDTO.userEmail != ''
                and not contactFormDTO.userEmail.isspace())

    def userEmailMatchesEmailRegex(self, userEmail: str) -> bool:
        re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

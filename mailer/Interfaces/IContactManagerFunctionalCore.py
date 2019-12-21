#IContactManagerFunctionalCore
import abc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailer.DTOs import ContactFormDTO


class IContactManagerFunctionalCore(abc.ABC):

    @abc.abstractmethod
    def userEmailUserGivenNameUserMessageAreAllPresentAndAreStrings(self, contactFormDTO: ContactFormDTO) -> bool:
        pass

    @abc.abstractmethod
    def getResponseCodeForCaseWhereContactFormInputsAreNotPresent(self, contactFormDTO: ContactFormDTO) -> int:
        pass

    @abc.abstractmethod
    def userEmailMatchesEmailRegex(self, userEmail) -> bool:
        pass

    @abc.abstractmethod
    def GenerateMimeMessageForContacted(self, contactFormDTO: ContactFormDTO) -> MIMEMultipart:
        pass

    @abc.abstractmethod
    def GenerateMimeMessageForUser(self, contactFormDTO: ContactFormDTO, HTMLTemplate=None) -> MIMEMultipart:
        pass

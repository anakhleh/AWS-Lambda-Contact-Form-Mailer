#ContactFormDTO.py

class ContactFormDTO:
    """Represents the data on a contact form on a website"""

    def __init__(self,
                 userEmail: str = "",
                 userGivenName: str = "",
                 userMessage: str = ""):
        self.userEmail = userEmail
        self.userGivenName = userGivenName
        self.userMessage = userMessage


# AWS-Lambda-Contact-Form-Mailer (Still WIP)

This is a description of the architecture, setup,
and code used to set up a contact-form mailer.

#What do I get when I set this up?
You have a contact form on your site.
The user enters info and hits send.
AWS gets it, sends them the confirmation that the email has been sent,
then AWS sends you an email, sends you an MMS message (text to your phone,
so you know you got contacted, and the user gets a confirmation email.

#Steps

#High Level Architecture
The architecture of the system is composed of four parts: 
a 'queuer' lambda, an SQS fifo queue, and a mailer lambda, and an API Gateway,

##The Queuer
The User sends a message using the contact form. The queue gets the message,
gets the required parameters from the message, sends the message over to the SQS queue,
and then returns a response to the user.

The reason we do this is because SMTP mailing is slow (anywhere from 4-10 seconds
to send all the messages we want to send) and the user expects quick feedback.

##The SQS Queue
A queue to handle multiple messages coming in at the same time.

##The Mailer
A lambda that receives messages from the SQS Queue,
then mails out the necessary emails and MMS-es.
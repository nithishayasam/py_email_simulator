# This code defines an Email class that represents an email message.
#  The class has attributes for the sender, receiver, subject, body, and read status of the email.
#  It also includes methods to mark the email as read, display the email content, 
# send an email, receive an email, read an email,delete an email,id,stamp.
#  The __str__ method provides a string representation of the email for easy display.
# I  would work on improvising this specific project for the next couple of days to make it more robust and functional.

import datetime

class Email:

    next_id = 1

    def __init__(self,sender, receiver,subject,body):

        # input validation

        if not sender:
            raise ValueError("Sender cannot be empty.")
        if not receiver:
            raise ValueError("Receiver cannot be empty.")
        
        # auto-incrementing email ID

        self.id = Email.next_id
        Email.next_id += 1
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        # Timestamp for when the email is created
        self.timestamp = datetime.datetime.now()

    def mark_as_read(self):
        self.read = True

    def display_email(self):  
        print(f"Email ID : {self.id}")
        print(f"From     : {self.sender}")
        print(f"To       : {self.receiver}")
        print(f"Subject  : {self.subject}")
        print(f"Body     : {self.body}")
        print(f"Time     : {self.timestamp.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Read     : {'Yes' if self.read else 'No'}")


    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"[{status}] From: {self.sender}, To: {self.receiver}, Subject: {self.subject}"    


    def send_email(self,receiver,subject,body):
        email = Email(
              sender=self.sender,
              receiver=receiver,
              subject=subject,
              body=body
              )
        
        print(f"Email sent to {receiver} with subject: {subject} and body: {body}")
        return email
    

    def receive_email(self,sender,subject,body):
        email = Email(
              sender=sender,
              receiver=self.receiver,
              subject=subject,
              body=body
              )
        
        print(f"Email received from {sender} with subject: {subject} and body: {body}")
        return email
    

    def read_email(self,email):
        email.mark_as_read()
        print("\n Reading Email:")
        email.display_email()


    def delete_email(self,email):
        print(f"Email from {email.sender} with subject: {email.subject} has been deleted.")    

email1 = Email(
    "alice@gmail.com",
    "bob@gmail.com",
    "Meeting",
    "Let's meet tomorrow."
)

print(email1)

sent_email = email1.send_email(
    "charlie@gmail.com",
    "Hello",
    "How are you?"
)

email1.read_email(sent_email)
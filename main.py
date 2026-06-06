

import datetime

class Email:
    next_id = 1

    def __init__(self,sender, receiver,subject,body):
        # input validation
        if not sender:
            raise ValueError("Sender cannot be empty.")
        if not receiver:
            raise ValueError("Receiver cannot be empty.")
        # auto-incrementing email ID"
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

    def get_email_details(self):  
        return(
        f"Email ID : {self.id}\n"
        f"From     : {self.sender}\n"
        f"To       : {self.receiver}\n"
        f"Subject  : {self.subject}\n"
        f"Body     : {self.body}\n"
        f"Time     : {self.timestamp.strftime('%d-%m-%Y %H:%M:%S')}\n"
        f"Read     : {'Yes' if self.read else 'No'}")
    
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
        if not isinstance(email, Email):
            raise TypeError("Expected an Email object.")
        
        email.mark_as_read()
        print("\n Reading Email:")
        print(email.get_email_details())

    def delete_email(self,email):
        if not isinstance(email, Email):
            raise TypeError("Expected an Email object.")
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
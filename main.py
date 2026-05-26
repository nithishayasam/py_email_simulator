# This code defines an Email class that represents an email message.
#  The class has attributes for the sender, receiver, subject, body, and read status of the email.
#  It also includes methods to mark the email as read, display the email content, send an email, receive an email, read an email, and delete an email.
#  The __str__ method provides a string representation of the email for easy display.
# I  would work on improvising this specific project for the next couple of days to make it more robust and functional.

class Email:
    def __init__(self,sender, receiver,subject,body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_email(self):  
        self.mark_as_read()  
        print(f"From: {self.sender}")
        print(f"To: {self.receiver}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")
        print(f"Read: {'Yes' if self.read else 'No'}")

    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"[{status}] From: {self.sender}, To: {self.receiver}, Subject: {self.subject}"    

    def send_email(self,receiver,subject,body):
        email = Email(sender=self,receiver=receiver,subject=subject,body=body)
        print(f"Email sent to {receiver} with subject: {subject} and body: {body}")

    def receive_email(self,sender,subject,body):
        email = Email(sender=sender,receiver=self,subject=subject,body=body)
        print(f"Email received from {sender} with subject: {subject} and body: {body}")

    def read_email(self,email):
        print(f"Reading email from {email.sender} with subject: {email.subject} and body: {email.body}")

    def delete_email(self,email):
        print(f"Email from {email.sender} with subject: {email.subject} has been deleted.")    


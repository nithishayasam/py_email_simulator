import datetime


class Email:
    next_id = 1

    def __init__(self, sender, receiver, subject, body):

        if not sender:
            raise ValueError("Sender cannot be empty.")

        if not receiver:
            raise ValueError("Receiver cannot be empty.")

        self.id = Email.next_id
        Email.next_id += 1

        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

        self.read = False
        self.timestamp = datetime.datetime.now()

    def mark_as_read(self):
        self.read = True

    def get_email_details(self):
        return (
            f"Email ID : {self.id}\n"
            f"From     : {self.sender}\n"
            f"To       : {self.receiver}\n"
            f"Subject  : {self.subject}\n"
            f"Body     : {self.body}\n"
            f"Time     : {self.timestamp.strftime('%d-%m-%Y %H:%M:%S')}\n"
            f"Read     : {'Yes' if self.read else 'No'}"
        )

    def __str__(self):
        status = "Read" if self.read else "Unread"

        return (
            f"[{status}] "
            f"{self.timestamp.strftime('%d-%m-%Y %H:%M:%S')} | "
            f"From: {self.sender} | "
            f"To: {self.receiver} | "
            f"Subject: {self.subject}"
        )

    def send_email(self, receiver, subject, body):

        email = Email(
            sender=self.sender,
            receiver=receiver,
            subject=subject,
            body=body
        )

        print(
            f"Email sent to {receiver} "
            f"with subject: {subject}"
        )

        return email

    def receive_email(self, sender, subject, body):

        email = Email(
            sender=sender,
            receiver=self.receiver,
            subject=subject,
            body=body
        )

        print(
            f"Email received from {sender} "
            f"with subject: {subject}"
        )

        return email

    def read_email(self):
        self.mark_as_read()

        print("\nReading Email:")
        print(self.get_email_details())


class Mailbox:

    def __init__(self):
        self.emails = []

    def add_email(self, email):

        if not isinstance(email, Email):
            raise TypeError("Expected an Email object.")

        self.emails.append(email)

        print(
            f"Email from {email.sender} "
            f"added to mailbox."
        )

    def sort_emails_by_time(self, newest_first=True):

        self.emails.sort(
            key=lambda email: email.timestamp,
            reverse=newest_first
        )

    def show_inbox(self):

        self.sort_emails_by_time()

        print("\nInbox:")

        if not self.emails:
            print("Inbox is empty.")
            return

        for email in self.emails:
            print(email)

    def delete_email(self, email_id):

        for email in self.emails:

            if email.id == email_id:

                self.emails.remove(email)

                print(
                    f"Email with ID {email_id} "
                    f"has been deleted."
                )

                return True

        print(f"Email with ID {email_id} not found.")
        return False

    def find_email(self, email_id):

        for email in self.emails:

            if email.id == email_id:
                return email

        return None

    def total_emails(self):
        return len(self.emails)



# Testing the System
# --------------------------

mailbox = Mailbox()

email1 = Email(
    "alice@gmail.com",
    "bob@gmail.com",
    "Meeting",
    "Let's meet tomorrow."
)

email2 = email1.send_email(
    "charlie@gmail.com",
    "Hello",
    "How are you?"
)

email3 = email1.send_email(
    "david@gmail.com",
    "Project Update",
    "Project completed successfully."
)

email4 = email1.send_email(
    "eva@gmail.com",
    "Reminder",
    "Meeting at 5 PM."
)

# Add emails to mailbox

mailbox.add_email(email2)
mailbox.add_email(email3)
mailbox.add_email(email4)

# Show inbox before reading

mailbox.show_inbox()

# Read one email

email3.read_email()

# Show inbox again
# email3 should now appear as Read

mailbox.show_inbox()

# Delete one email

mailbox.delete_email(email2.id)

# Show inbox after deletion

mailbox.show_inbox()

print(
    "\nTotal Emails in Mailbox:",
    mailbox.total_emails()
)
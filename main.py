
import datetime
import uuid


class Email:
    """Represents a single email message."""

    def __init__(self, sender, receiver, subject, body):

        if not sender or not sender.strip():
            raise ValueError("Sender cannot be empty.")

        if not receiver or not receiver.strip():
            raise ValueError("Receiver cannot be empty.")

        if not subject or not subject.strip():
            raise ValueError("Subject cannot be empty.")

        self.id = str(uuid.uuid4())[:8]   # Unique 8-char ID, no collision risk
        self.sender = sender.strip()
        self.receiver = receiver.strip()
        self.subject = subject.strip()
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

    def read_email(self):
        """Mark email as read and display its details."""
        self.mark_as_read()
        print("\nReading Email:")
        print(self.get_email_details())

    def __str__(self):
        status = "Read  " if self.read else "Unread"
        return (
            f"[{status}] "
            f"{self.timestamp.strftime('%d-%m-%Y %H:%M:%S')} | "
            f"ID: {self.id} | "
            f"From: {self.sender} | "
            f"To: {self.receiver} | "
            f"Subject: {self.subject}"
        )


class User:
    """
    Represents an email user who can send and receive emails.
    Sending/receiving logic belongs here, NOT on the Email object.
    """

    def __init__(self, email_address):
        if not email_address or not email_address.strip():
            raise ValueError("Email address cannot be empty.")
        self.email_address = email_address.strip()

    def send_email(self, receiver, subject, body):
        """Create and return a new Email from this user to a receiver."""
        email = Email(
            sender=self.email_address,
            receiver=receiver,
            subject=subject,
            body=body
        )
        print(f"✉  Email sent from {self.email_address} to {receiver} | Subject: '{subject}'")
        return email

    def receive_email(self, sender, subject, body):
        """Create and return a new Email received by this user."""
        email = Email(
            sender=sender,
            receiver=self.email_address,
            subject=subject,
            body=body
        )
        print(f"📥 Email received by {self.email_address} from {sender} | Subject: '{subject}'")
        return email

    def __str__(self):
        return f"User({self.email_address})"


class Mailbox:
    """Stores and manages a collection of Email objects."""

    def __init__(self):
        self.emails = []

    def add_email(self, email):
        if not isinstance(email, Email):
            raise TypeError("Expected an Email object.")
        self.emails.append(email)
        print(f"📬 Email from '{email.sender}' added to mailbox.")

    def sort_emails_by_time(self, newest_first=True):
        self.emails.sort(key=lambda e: e.timestamp, reverse=newest_first)

    def show_inbox(self):
        self.sort_emails_by_time()
        print("\n" + "=" * 70)
        print("INBOX")
        print("=" * 70)
        if not self.emails:
            print("  Inbox is empty.")
        else:
            for email in self.emails:
                print(" ", email)
        print(f"\n  Total: {self.total_emails()} email(s) | Unread: {self.unread_count()}")
        print("=" * 70)

    def delete_email(self, email_id):
        """
        Safely delete email by ID.
        Uses list comprehension — avoids mutating list during iteration.
        """
        original_count = len(self.emails)
        self.emails = [e for e in self.emails if e.id != email_id]

        if len(self.emails) < original_count:
            print(f"🗑  Email with ID '{email_id}' has been deleted.")
            return True
        else:
            print(f"⚠  Email with ID '{email_id}' not found.")
            return False

    def find_email(self, email_id):
        """Return Email object by ID, or None if not found."""
        for email in self.emails:
            if email.id == email_id:
                return email
        return None

    def total_emails(self):
        return len(self.emails)

    def unread_count(self):
        """Return number of unread emails."""
        return sum(1 for e in self.emails if not e.read)


# -------------------------------------------------------
# Demo / Testing
# -------------------------------------------------------

print("\n" + "=" * 70)
print("EMAIL SIMULATOR — DEMO")
print("=" * 70)

# Create users
alice = User("alice@gmail.com")
bob   = User("bob@gmail.com")

# Alice sends emails to different people
email1 = alice.send_email("bob@gmail.com",     "Meeting",        "Let's meet tomorrow.")
email2 = alice.send_email("charlie@gmail.com", "Hello",          "How are you?")
email3 = alice.send_email("david@gmail.com",   "Project Update", "Project completed successfully.")
email4 = alice.send_email("eva@gmail.com",     "Reminder",       "Meeting at 5 PM.")

# Bob receives an email from charlie
email5 = bob.receive_email("charlie@gmail.com", "Re: Hello", "I'm doing great, thanks!")

# Set up bob's mailbox
mailbox = Mailbox()
mailbox.add_email(email1)
mailbox.add_email(email2)
mailbox.add_email(email3)
mailbox.add_email(email4)
mailbox.add_email(email5)

# Show inbox before reading
mailbox.show_inbox()

# Read one email
email3.read_email()

# Show inbox again — email3 should now appear as Read
mailbox.show_inbox()

# Delete one email using its ID
mailbox.delete_email(email2.id)

# Try deleting a non-existent ID to test the warning
mailbox.delete_email("nonexistent")

# Show final inbox
mailbox.show_inbox()

# Find an email by ID and read it
found = mailbox.find_email(email4.id)
if found:
    print(f"\n Found email: {found}")
    found.read_email()
else:
    print("\n Email not found.")
# Script to check the validity of an email address using basic and regex-based methods
from utilities.email_utils import is_valid_email_basic, is_valid_email

# generate a list of emails to check
list_of_emails = ['test@example.com', 'invalid-email', 'user@domain.org', 'another@test.net']
if __name__ == "__main__":
    for email in list_of_emails:
        if is_valid_email_basic(email):
            print(f"{email} is VALID (Basic Check)")
        else:
            print(f"{email} is INVALID (Basic Check)")

        if is_valid_email(email):
            print(f"{email} is VALID (Regex Check)")
        else:
            print(f"{email} is INVALID (Regex Check)")
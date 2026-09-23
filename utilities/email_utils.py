
def is_valid_email_basic(email):
    if email.find('@') == -1 or email.count('@') != 1:
        return False
    else:
        return True

def is_valid_email():
    pass

def extract_username(email):
    if is_valid_email_basic(email):
        return email[:email.find('@')]

    return "INVALID"

if __name__ == '__main__':
    email = input("Enter your email ID: ")
    if is_valid_email_basic(email):
        print(f"{email} is VALID")
    else:
        print(f"{email} is INVALID")
# import utilities.email_utils

# print(utilities.email_utils.is_valid_email_basic("john.doe@gmail.com"))

# from utilities.email_utils import is_valid_email_basic 

# print(is_valid_email_basic("john.doe@email.com"))

# from utilities.email_utils import is_valid_email_basic  as isvalidemail
from utilities import is_valid_ip, is_valid_email_basic, extract_username

print(is_valid_email_basic("john.doe@email.com"))
# TODO: Create a list of email addresses and print whether they are valid or not
# Include both valid and invalid email addresses examples 
# Also printing of Usernames

# Solution
emails = ["vishwas@cloudthat.com", "johncom", ""]

from utilities.email_utils import extract_username
from utilities.ip_utils import is_valid_ip

print(f"Username for {"vishwas@cloudthat.com"} is {extract_username("vishwas@cloudthat.com")}")
ip_add = "192.168.1.1"
# TODO: Create a list of IP addresses and print whether they are valid or not
# Include both valid and invalid IP addresses examples 

if is_valid_ip(ip_add):
    print(f"{ip_add} is VALID")
else:
    print(f"{ip_add} is INVALID")
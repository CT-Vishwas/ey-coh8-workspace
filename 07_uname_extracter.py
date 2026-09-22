email = input("Enter your email ID: ")

if email.find('@') == -1 or email.count('@') != 1:
    print("Invalid Email ID")
else:
    print("Valid Email ID")
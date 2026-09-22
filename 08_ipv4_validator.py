
ipv4_address = input("Enter the IPv4 Address: ")

if not ipv4_address.count('.') == 3:
    print("INVALID")
    exit(0)

parts = ipv4_address.split('.')
for i in range(len(parts)):
    field = parts[i]
    if not (field.isdigit() and int(field) >= 0 and int(field) <= 255):
        print("INVALID")
        exit(0)

print("VALID")
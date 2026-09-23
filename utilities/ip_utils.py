def is_valid_ip(ipv4_address):
    if not ipv4_address.count('.') == 3:
        return False

    parts = ipv4_address.split('.')
    for i in range(len(parts)):
        field = parts[i]
        if not (field.isdigit() and int(field) >= 0 and int(field) <= 255):
            return False

    return True
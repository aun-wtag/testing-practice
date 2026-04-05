import re

def check_valid_email(email):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[-]?\w+[.]\w{2,3}$"
    if re.search(regex, email):
        return True
    else:
        return False
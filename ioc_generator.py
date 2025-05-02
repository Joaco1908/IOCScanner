import re
import json
import ipaddress


# --- Validation helpers ---


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def is_valid_hash(h):
    h = h.lower()
    if len(h) == 32 and re.fullmatch(r"[a-f0-9]{32}",h): #MD5
        return True
    if len(h) == 40 and re.fullmatch(r"[a-f0-9]{40}",h): #SHA1
        return True
    if len(h) == 64 and re.fullmatch(r"[a-f0-9]{64}",h): #SHA256
        return True
    return False

# --- Main script logic ---

def Main():
    
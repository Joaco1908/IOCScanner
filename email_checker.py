import re
import argparse
import os
import sys
from rich import print
import dns.resolver
import requests

IPQS_API_KEY = os.getenv("IPQS_API_KEY")

# Check if the email has a valid format
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# Check if the domain can receive emails (MX record)
def domain_exists(email):
    try:
        domain = email.split('@')[1]
        dns.resolver.resolve(domain, 'MX')
        return True
    except Exception:
        return False

# Check email reputation using IPQualityScore API
def check_ipqs_email(email):
    if not IPQS_API_KEY:
        return {"error": "API key not found"}
    
    url = f"https://ipqualityscore.com/api/json/email/{IPQS_API_KEY}/{email}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Email verification with format, domain and IPQS reputation.")
    parser.add_argument('-t', '--textfile', type=str, help="Text file with email addresses.")
    args = parser.parse_args()

    emails = []

    if args.textfile:
        if not os.path.exists(args.textfile):
            print(f"\n[red][!] Error: File '{args.textfile}' does not exist.[/]")
            sys.exit(1)
        if not args.textfile.lower().endswith(".txt"):
            print("\n[red][!] The text file must have a .txt extension.[/]")
            sys.exit(1)
        with open(args.textfile, "r") as f:
            emails = [line.strip() for line in f if line.strip()]
    else:
        print(f"\n[green][+] Enter the email address to check: ", end="")
        emails = [input().strip()]

    for email in emails:
        print(f"\n[blue]🔍 Checking {email}...[/]")

        if is_valid_email(email):
            print(f"[green]Format is valid[/]")

            if domain_exists(email):
                print(f"[green]Domain exists[/]")
            else:
                print(f"[red]Domain does not exist[/]")

            result = check_ipqs_email(email)
            if "error" in result:
                print(f"[red]IPQS API error: {result['error']}[/]")
            else:
                if result.get("suspect", False):
                    print(f"[red]Suspicious email (reason: {result.get('frequent_complainer_reason', 'unknown')})[/]")
                else:
                    print(f"[green]Email seems clean according to IPQS[/]")
        else:
            print(f"[red]Invalid email format[/]")

if __name__ == "__main__":
    main()

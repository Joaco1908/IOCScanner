from rich import print
import argparse 
import os
import sys
import requests
import json

# Load API Key
API_KEY = os.getenv("56196dcb827275848d97dd1c6c0dcabff3b99257ee0bcfb3a65f5abbba2f9ade64f3c3fd71b77f25")

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": "90"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()["data"]
            return {
                    "ip": data["ipAddress"],
                    "abuseScore": data["abuseConfidenceScore"],
                    "totalReports": data["totalReports"],
                    "country": data.get("countryCode", "N/A"),
                    "isp": data.get("isp", "N/A"),
                    "lastReportedAt": data.get("lastReportedAt", "N/A")
                }
        else:
            print(f"[red]Request failed for {ip}: {response.status_code}[/]")
            return {
                    "ip": ip,
                    "error": f"HTTP {response.status_code}"
                }
    except requests.RequestException as e:
        print(f"[red][!] Network error while checking {ip}: {e}[/]")
        return {
            "ip": ip,
            "error": str(e)
        }


def main():
    parser = argparse.ArgumentParser(description="Check IP reputation using AbuseIPDB")

    parser.add_argument('-t', '--textfile', type=str, help="Name of the textfile with the IPs.")

    args = parser.parse_args()

    ips = []

    if (args.textfile):
        # If there is a text file
        if (not os.path.exists(args.textfile)):
            print(f"\n[red][!] Error: File '{args.textfile}' does not exist.[/]")
            sys.exit(1)
        if (not args.textfile.lower().endswith(".txt")):
            print("\n[red][!] Error: The textfile must have a .txt extension.[/]")
            sys.exit(1)
        with open(args.textfile, "r") as f:
            ips = [line.strip() for line in f if line.strip()]
    else:
        # If there is no text file (gather IPs from console)
        print(f"\n[green][+] Give me the IP that you want to check: ", end="")
        text_console = input()
        ips = [text_console.strip()]
    results = []
    for ip in ips:
        print(f"\n[green]Checking {ip}...[/]")
        result = check_ip(ip)
        if "error" in result:
            print(f"[yellow]Error with {ip}: {result['error']}[/]")
        else:
            score = result["abuseScore"]
            color = "red" if score >= 85 else "green"

            print(f"\n[{color}]{ip} → Score: {score} | Reports: {result['totalReports']} | Country: {result['country']}[/]")
            if score >= 85:
                print(f"\n[red]High risk: this IP is highly likely to be malicious.[/]")
            else:
                print(f"\n[green]This IP appears clean — no signs of abuse detected.[/]")
        results.append(result)


if __name__ == "__main__":
    main()

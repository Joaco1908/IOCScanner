import argparse
from pathlib import Path
import hashlib 
import json
from rich import print
import os
import sys

# Argument parser

parser = argparse.ArgumentParser(description="Scan a directory for malicious files.")
parser.add_argument("--path", "-p", required=True, help="Path to the directory to scan")
parser.add_argument("--iocs", "-i", required=True, help="Path to the iocs.json file")
args = parser.parse_args() 

target_directory = Path(args.path)
ioc_file_path = args.iocs

# Load IoCs
if (not os.path.exists(ioc_file_path)):
    print(f"\n[red][!] Error: File '{ioc_file_path}' does not exist.[/]")
    sys.exit(1)

with open(ioc_file_path, "r") as f:
    iocs = json.load(f)

print(f"\n[green][+] File '{ioc_file_path}' found.[/]")

if (not os.path.exists(target_directory)):
    print(f"\n[red][!] Error: Directory '{target_directory}' does not exist.[/]")
    sys.exit(1)

print(f"\n[green][+] Directory '{target_directory}' found. Starting scan. [/]")

# Scanning
for path in target_directory.rglob("*"):
    if path.is_file():
        filename = path.name
        filesize = path.stat().st_size
        try:
            with open(path, "rb") as f:
                content = f.read()
 
                md5 = hashlib.md5(content).hexdigest()
                sha1 = hashlib.sha1(content).hexdigest()
                sha256 = hashlib.sha256(content).hexdigest()

                checks = {
                    "md5": ("hashes", md5),
                    "sha1": ("hashes", sha1),
                    "sha256": ("hashes", sha256),
                    "filename": ("filenames", filename),
                    "file size": ("file sizes", filesize),
                }

                matched = False
                for label, (ioc_key, value) in checks.items():
                    if value in iocs.get(ioc_key, []):
                        if not matched:
                            print(f"\n[red][!] Suspicious file found: {path}[/]")
                            matched = True
                        print(f"[red]{label} matched: {value}")

        
        except Exception as e:
            print(f"\n[red]Error reading file {path}: {e}[/]")
        


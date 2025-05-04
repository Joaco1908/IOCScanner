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

# Scanning
for path in target_directory.rglob("*"):
    if path.is_file():
        filename = path.name
        filesize = path.stat().st_size
        try:
            with open(path, "rb") as f: # "rb" = read binary, para leer ejecutables, imagenes, etc
                content = f.read() # Content ahora es un bytes object que se puede usar para calcular hashes
 
                md5 = hashlib.md5(content).hexdigest()
                sha1 = hashlib.sha1(content).hexdigest()
                sha256 = hashlib.sha256(content).hexdigest()

                if (
                    (md5 in iocs["hashes"]) or 
                    (sha1 in iocs["hashes"]) or 
                    (sha256 in iocs["hashes"]) or

                    (filename in iocs["filenames"]) or

                    (filesize in iocs["file sizes"])
                ):
                    print(f"\n[red][!] File matched! {path}[/]")
        except Exception as e:
            print(f"\n[red]Error reading file {path}: {e}[/]")
        


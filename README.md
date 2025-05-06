# ThreatKit 🛡️

**ThreatKit** is a Python-based tool designed to help Blue Team analysts detect malicious files and investigate Indicators of Compromise (IoCs) on local systems. The project is divided into three independent modules:

- `ioc_generator.py` → Validate and store IoCs in a JSON file  
- `ioc_scanner.py` → Analyze a directory for suspicious files based on IoCs  
- `ip_checker.py` → Query IPs against AbuseIPDB to check for malicious behavior
- `email_checker.py` →  Validate email format, check domain existence, and analyze email reputation using IPQualityScore

---

## 🔍 Features

- Support for the following IoC types:
  - IP addresses (validated with `ip_checker.py`)
  - File hashes (MD5, SHA1, SHA256)
  - Suspicious file names
  - File size value
- Works entirely offline (except for IP/email reputation check email dns resolver)

---

## 🚀 How to Use

ThreatKit is divided into three modules. You can run each one independently depending on your task.

🧩 1. Generate IoCs – ioc_generator.py
Use this module to create or validate IoC entries and store them in a JSON file. <br>
Flags:
- `--output` (`-o`): Specifies the name of the output JSON file where the IoCs will be saved. In this example, the IoCs will be saved in test.json.
- `--append` (`-a`): Adds the new IoCs to the existing JSON file instead of overwriting it.

🔎 2. Scan Files – ioc_scanner.py
Use this module to scan a directory for files that match any of the IoCs defined in a JSON file. <br>
Flags:
- `--path` (`-p`): Specifies the path to the directory you want to scan. For example, test is the directory where the files to be checked are located.

- `--ioc_file` (`-i`): Specifies the path to the IoC JSON file you want to use for the scan. In this case, test.json contains the IoCs that will be checked against the files in the specified directory.

🌐 3. Check IP Reputation – ip_checker.py
Use this module to check IP addresses against AbuseIPDB for reputation scoring.
Flag:
- `--textfile` (`-t`): Specifies a .txt file containing a list of IP addresses. The script will read each IP from the file and check its reputation using the configured threat intelligence API.

How to integrate API key: <br> <br>
Create an account at https://abuseipdb.com and generate your API key. <br>
Set the API key as an environment variable in your terminal:  <br> <br>
Windows (Command Prompt or PowerShell): `set ABUSEIPDB_API_KEY=YOUR_KEY` <br> <br>
Linux/macOS (Bash/Zsh): `export ABUSEIPDB_API_KEY=YOUR_KEY` <br> <br>
Replace YOUR_KEY with the actual key you obtained from AbuseIPDB.

---
## ✅ Example

This test was conducted on my WSL Linux machine. We created a test directory containing five subdirectories, each with a mix of safe and malicious files. A test.json file was also created for use in this test.

Creating testa.json to demonstrate how to build custom IoC JSON files. <br>
<img src="https://github.com/user-attachments/assets/58055b59-9516-42b6-95b5-1081273c82a7" width="600"/>

A look at the contents of testa.json. <br> 
<img src="https://github.com/user-attachments/assets/ba3ce801-1ad5-40d4-a5cc-de7400620a13" width="600"/>

Demonstrating how ioc_scanner.py analyzes the test directory using test.json, which contains IoCs, against a set of existing safe and malicious files. <br>
<img src="https://github.com/user-attachments/assets/02d67b95-e9b9-45eb-aba7-86f8d69ca64c" width="600"/>

🛡️ IP_Checker Example <br>
Using it from the console: <br>
Provide a single IP directly via interactive input: <br>
<img src="https://github.com/user-attachments/assets/ab33a88b-a95b-4fe9-93e5-fade1b3db506" width="600"/>

Using it with a text file: <br>
Create a file (like text.txt) containing one IP per line: <br>
<img src="https://github.com/user-attachments/assets/66e36e31-1baa-461c-966f-8c8d559aa4b9" width="600"/> <br>
Run the script and pass the file as an argument. <br>
Result output: <br>
<img src="https://github.com/user-attachments/assets/0c031a77-aebc-4544-91b7-24c3f6d514b2" width="600"/>

---

## ⚙️ Requirements

- Python 3.8+
- [`AbuseIPDB`](https://www.abuseipdb.com/) (for IP reputation checks)

Install dependencies:

```bash 
pip install requests rich os sys json argparse pathlib hashlib
```

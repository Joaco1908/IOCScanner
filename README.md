# ThreatKit 🛡️

**ThreatKit** is a Python-based tool designed to help Blue Team analysts detect malicious files and investigate Indicators of Compromise (IoCs) on local systems. The project is divided into four independent modules:

- `ioc_generator.py` → Validate and store IoCs in a JSON file  
- `ioc_scanner.py` → Analyze a directory for suspicious files based on IoCs  
- `ip_checker.py` → Query IPs against AbuseIPDB to check for malicious behavior  
- `email_checker.py` → Validate email format, check domain existence, and analyze email reputation using IPQualityScore

---

## 🔍 Features

- Support for the following IoC types:
  - IP addresses (validated with `ip_checker.py`)
  - File hashes (MD5, SHA1, SHA256)
  - Suspicious file names
  - File size value
- Offline support (only `ioc_scanner.py` is fully offline; IP/email reputation checks require internet access)

---

## 🚀 How to Use 

ThreatKit is divided into four modules. You can run each one independently depending on your task.

---

### 🧩 1. Generate IoCs – `ioc_generator.py`

Use this module to create or validate IoC entries and store them in a JSON file.

**Flags:**

- `--output` (`-o`): Name of the output JSON file where the IoCs will be saved.  
- `--append` (`-a`): Adds the new IoCs to the existing JSON file instead of overwriting it.

---

### 🔎 2. Scan Files – `ioc_scanner.py`

Use this module to scan a directory for files that match any of the IoCs defined in a JSON file.

**Flags:**

- `--path` (`-p`): Directory to scan.  
- `--ioc_file` (`-i`): Path to the IoC JSON file.

---

### 🌐 3. Check IP Reputation – `ip_checker.py`

Use this module to check IP addresses against AbuseIPDB for threat intelligence.

**Flag:**

- `--textfile` (`-t`): A `.txt` file with one IP per line.

**API Setup:**

1. Create an account at [https://abuseipdb.com](https://abuseipdb.com)  
2. Get your API key  
3. Set it as an environment variable:

```bash
# Windows
set ABUSEIPDB_API_KEY=YOUR_KEY

# Linux/macOS
export ABUSEIPDB_API_KEY=YOUR_KEY
```

---

### ✉️ 4. Email Validity & Reputation Checker – `email_checker.py`

This script validates email addresses by combining syntax checks, DNS lookups, and reputation analysis via IPQualityScore.

**🔍 Validation steps:**

- ✅ **Format check** using regular expressions
- ✅ **Domain verification** via DNS MX records
- 🌐 **Reputation check** using [IPQualityScore Email Validation API](https://www.ipqualityscore.com/)

---

#### 🛠️ How to Use

**Option 1 – From a file:**

```bash
python email_checker.py --textfile emails.txt
```

`emails.txt` should be a plain text file with one email address per line.

**Option 2 – Manual input:**

```bash
python email_checker.py
```

The script will prompt you to enter an email address via console.

**🔐 API Setup (IPQualityScore):**

1. Sign up for a free account at [ipqualityscore.com](https://www.ipqualityscore.com)
2. Copy your API key from the dashboard
3. Set it as an environment variable:

```bash
# On Windows
set IPQS_API_KEY=your_key

# On Linux/macOS
export IPQS_API_KEY=your_key
```
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

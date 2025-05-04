# ThreatKit 🛡️

**ThreatKit** is a Python-based tool designed to help Blue Team analysts detect malicious files and investigate Indicators of Compromise (IoCs) on local systems. The project is divided into three independent modules:

- `ioc_generator.py` → Validate and store IoCs in a JSON file  
- `ioc_scanner.py` → Analyze a directory for suspicious files based on IoCs  
- `ip_checker.py` → Query IPs against AbuseIPDB to check for malicious behavior

---

## 🔍 Features

- Support for the following IoC types:
  - IP addresses (validated with `ipaddress`)
  - Emails (validated with regex)
  - File hashes (MD5, SHA1, SHA256)
  - Suspicious file names
- Works entirely offline (except for IP reputation check)

---

## ⚙️ Requirements

- Python 3.8+
- [`AbuseIPDB`](https://www.abuseipdb.com/) (for IP reputation checks)

Install dependencies:

```bash 
pip install requests rich os sys 
```

## Example

This test is made in my WSL linux machine. 
We created a test directory with another 5 directories that contains both safe and malicious file. We also made a test.json file for this test.

# IOCScanner 🛡️

**IOCScanner** is a Python-based tool designed to help Blue Team analysts detect malicious files and investigate Indicators of Compromise (IoCs) on local systems. The project is divided into three independent modules:

- `ioc_generator.py` → Validate and store IoCs in a JSON file  
- `scan_filesystem.py` → Analyze a directory for suspicious files based on IoCs  
- `check_ip_reputation.py` → Query IPs against AbuseIPDB to check for malicious behavior

---

## 🔍 Features

- Support for the following IoC types:
  - IP addresses (validated with `ipaddress`)
  - Emails (validated with regex)
  - File hashes (MD5, SHA1, SHA256)
  - Suspicious file names
- Customizable and portable: no dependencies on commercial tools
- Works entirely offline (except for IP reputation check)
- Generates structured JSON reports

---

## ⚙️ Requirements

- Python 3.8+
- [`requests`](https://pypi.org/project/requests/) (for IP reputation checks)

Install dependencies:

```bash
pip install -r requirements.txt

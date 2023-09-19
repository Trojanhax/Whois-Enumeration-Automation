# Whois-Enumeration-Automation
## Introduction
Whois enumeration is a valuable technique for gathering domain registration information. It allows you to discover details about domain names, such as the domain owner's contact information, registration and expiration dates, and more. Manually performing Whois lookups can be time-consuming, but with this automation script, you can streamline the process and save the results for further analysis.

This Python script uses the python-whois library to automate Whois enumeration and save the information to a text file. It's a handy tool for cybersecurity professionals, domain administrators, and anyone interested in quickly retrieving domain registration details.

## Prerequisites
Before using this script, ensure you have the following prerequisites installed:

- Python 3.x
- python-whois library

You can install the required library using pip:
```bash
pip install python-whois
```

## Getting Started
Clone this repository or download the whois_enum_and_save.py script.

1. Open your terminal or command prompt.

2. Run the script with the desired domain name as an argument:

```bash
python whoisAuto.py example.com
```

Replace example.com with the domain name you want to perform a Whois lookup on.

1. The script will display the Whois information on the console and save it to a text file named "example.com_whois_info.txt" in the same directory as the script.
## Usage
The primary purpose of this script is to automate Whois enumeration for domain names. Here's the basic usage:

```bash
python whoisAuto.py <domain_name>
```
Replace <domain_name> with the target domain you want to perform a Whois lookup on.

## Examples
### Example 1: Perform a Whois Lookup for "example.com"
```bash
python whoisAuto.py example.com
```
This command will retrieve the Whois information for "example.com" and save it to a file named "example.com_whois_info.txt."

### Example 2: Perform a Whois Lookup for "example.org"

```bash
python whoisAuto.py example.org
```
This command will retrieve the Whois information for "example.org" and save it to a file named "example.org_whois_info.txt."

# Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request on the GitHub repository.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

import whois
import argparse

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return str(e)

def save_to_file(domain, whois_info):
    filename = f"{domain}_whois_info.txt"
    with open(filename, "w") as file:
        file.write("Whois Information for {}\n\n".format(domain))
        file.write(str(whois_info))

def main():
    parser = argparse.ArgumentParser(description="Automate Whois Enumeration")
    parser.add_argument("domain", help="Domain name to perform Whois lookup on")
    args = parser.parse_args()

    domain = args.domain

    print(f"Performing Whois lookup for {domain}...\n")

    whois_info = get_whois_info(domain)

    if isinstance(whois_info, str):
        print(f"Error: {whois_info}")
    else:
        print("Whois Information:")
        print(whois_info)
        save_to_file(domain, whois_info)
        print(f"\nWhois information saved to {domain}_whois_info.txt")

if __name__ == "__main__":
    main()

import requests
from urllib.parse import quote

def check_subdomains(domain, wordlist_file, output_file):
    with open(wordlist_file, 'r') as file:
        subdomains = file.read().splitlines()

    live_subdomains = []

    for subdomain in subdomains:
        url = f'http://{quote(subdomain)}.{domain}'
        try:
            response = requests.get(url)
            if response.status_code in range(200, 300):
                live_subdomains.append(url)
        except requests.exceptions.RequestException:
            pass

    with open(output_file, 'w') as file:
        for subdomain in live_subdomains:
            file.write(subdomain + '\n')

    print(f"Live subdomains have been saved to '{output_file}'.")

# Prompt for domain, wordlist file, and output file
domain = input('Enter the domain: ')
wordlist_file = input('Enter the wordlist file path: ')
output_file = input('Enter the output file path: ')

# Usage example:
check_subdomains(domain, wordlist_file, output_file)

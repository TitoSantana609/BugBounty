#!/bin/bash

# Prompt for the domain name
read -p "Enter the domain: " domain

# Run amass scan and save results to a file
amass enum -d "$domain" -o domains.txt

# Use HTTProbe to check for live subdomains and save results to another file
cat domains.txt | httprobe -c 50 -t 3000 > live_subdomains.txt

# Display the live subdomains
echo "Live subdomains:"
cat live_subdomains.txt

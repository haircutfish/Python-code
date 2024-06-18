#!/usr/bin/env python3

#Simple Python script used to defanging IP and Domain addresses
#Created by Dan R. 2024-01-15
#Updated 2024-06-18

import sys
import os

def addressDefanger(address):
    defang = address.replace('.', '[.]')
    return defang

if len(sys.argv) < 2:
    print('Please specify the file you want to defang the IPs/Domains')
    exit(1)

addressFile = sys.argv[1]

with open(addressFile, 'r') as file:
    lines = file.readlines()

for ip in lines:
    ip.strip()
    defanged_address = addressDefanger(ip)

print(defanged_address)

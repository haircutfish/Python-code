#!/usr/bin/env python3
# Written By Dan Rearden
# 2023-08-19


import sys
import subprocess
import time

# if no domain was given, it would output this to the console
if len(sys.argv) == 1:
        print("No Domain or IP address was giving.  Please try again.")
        exit()

# Starting the timer & Displaying it to the console
start_time = time.time()
print("***DomainChecker.py started at %s ***\n"%start_time)

print('*'*60 + "\n")

# retrieving the Domain name from the command line
domain_name = sys.argv[1]

# Funcition to repeat the command
def results(arg):
     length = len(arg)
     if length != 0:
        print(arg)
        print('*'*60 + "\n")
     else:
        print('No results found') 
        print('*'*60 + "\n")




whois = subprocess.getoutput('whois %s | egrep -i "Creation Date|created|Registrar Registration Expiration Date" | sed "s/^[[:blank:]]*//;s/[[:blank:]]*$//"'%domain_name)

print ("        ***Whois***")

results(whois)


# Run Curl command

curl = subprocess.getoutput('curl -IL --no-progress-meter %s | grep HTTP'%domain_name)

print('         ***Curl***')

results(curl)

# Run NSLookup Command

nslookup = subprocess.getoutput('nslookup %s | egrep "Non-authoritative answer|Address: "' %domain_name)

print('         ***NsLookup***')

results(nslookup)

# Run Host command

host = subprocess.getoutput('host %s'%domain_name)

print('          ***Host***')

results(host)

# Run Dig command

dig = subprocess.getoutput('dig -t any %s +short'%domain_name)

print('          ***Dig***')

results(dig)

# End time and output to 

endtime = time.time()

timelength = endtime - start_time

print("It took %s to complete"%timelength)

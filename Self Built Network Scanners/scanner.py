#!/bin/python3
import sys
import socket
from datetime import datetime as dt


#Define the target of the scan
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Make hostname into ipv4 (allows people to enter a domain)
else:
    print("Invalid amount of args")

#Add pretty banner
print("-" * 50)
print("Scanning Target " + target)
print("-" * 50)

try:
    for port in range(50,85): #running through 1 port at a time (slow)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        if result == 0:
            print("port {} is open".format(port))
        s.close

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Unable to Resolve hostname")
    sys.exit()

except socket.error:
    print("Unable to connect to target")
    sys.exit()

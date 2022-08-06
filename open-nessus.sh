#/bin/bash

#Starts and opens Nessus

echo"-------------------------------"
echo "Starting Nessus"
/bin/systemctl start nessusd.service
echo "Nessus Started"
echo "Go to https://kali:8834/"
google-chrome https://kali:8834/
echo"-------------------------------"

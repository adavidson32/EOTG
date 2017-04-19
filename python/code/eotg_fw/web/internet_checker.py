import os

hostname = "google.com"

#use & to run the ping in the background...
response = os.system("ping -c 1 "  + hostname + " &")

if response:
    print("No internet connection")
else:
    print("Internet is connected")

import requests
import urllib.parse
import urllib.request
import json
import sys

if len(sys.argv)==1:
  Device_ID = 1
else:
  print(type(Device_ID))
  Device_ID = sys.argv[1]
print("Device_ID: ", Device_ID)
Device_ID = str(Device_ID)

url_path = "/devices/getBrewSettings/"
url_base = "http://espressotg.info/eotg/api"
url_getBrewSettings = "%s%s%s" (url_base, url_path, Device_ID)
print(url_getBrewSettings)

response = urllib.request.urlopen(url_getBrewSettings)
body_json = response.read().decode()
body = json.loads(body_json)
print("Response from Server: " + str(body))

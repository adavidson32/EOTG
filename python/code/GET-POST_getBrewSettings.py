import requests
import urllib.parse
import urllib.request
import json
import sys

if len(sys.argv)==1:
  Device_ID = '1'
else:
  Device_ID = sys.argv[1]
print("Device_ID: ", Device_ID)

url_path = "/devices/getBrewSettings/"
url_base = "http://espressotg.info/eotg/api"
url_getBrewSettings = "%s%s%s" % (url_base, url_path, Device_ID)
print("Connecting to: ", url_getBrewSettings, ".....")

response = urllib.request.urlopen(url_getBrewSettings)
body_json = response.read().decode()
body = json.loads(body_json)
print("body type: ", type(body))
contents = body['brewSettings']
print("contents type: ", type(contents))
print("Data from Server: ", contents)
print("Length of contents: ", len(contents))

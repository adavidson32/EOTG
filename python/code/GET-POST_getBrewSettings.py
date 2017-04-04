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
contents = body['brewSettings']
print("Length of contents: ", len(contents))
print("")
print("Settings for Device #", Device_ID, "-------------------------------")
x = 1
for i in contents:
  print("  Setting #", x, " listed below:")
  print("      Setting ID:    ", i['id'])
  print("      Setting Value: ", i['brew_setting_value'])
  x++
print("")
print("-------------------------------------------------------------------")

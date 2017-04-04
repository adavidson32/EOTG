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
print(type(body_json))
body = json.loads(body_json)
print("body type: ", type(body))
for setting in body:
  print("Info for setting #", setting, " listed below:")
  print("    Setting ID:    ", setting['id'])
  print("    Setting Value: ", setting['brew_setting_value'])

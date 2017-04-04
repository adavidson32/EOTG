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
contents = body['brewSettings']
print("length of body: ", len(body))
print("length of contents: ", len(contents))
print("body type: ", type(body))
print("contents type: ", type(contents))
for i in contents:
  print(i)
  print(i['id'])
#  print("Info for setting #", i, " listed below:")
#  print("    Setting ID:    ", i['id'])
#  print("    Setting Value: ", i['brew_setting_value'])

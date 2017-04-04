import requests
import urllib.parse
import urllib.request
import json

url_path = "/devices/getBrewSettings/
url_base = "http://espressotg.info/eotg/api"
url_getBrewSettings = "%s%s%s" (url_base, url_path, Device_ID)

response = urllib.request.urlopen(url_getBrewSettings)
body_json = response.read().decode()
body = json.loads(body_json)
print("Response from Server: " + str(body))

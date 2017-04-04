import requests
import json

def getMAC(interface):
  try:
    str = open('/sys/class/net/' + interface + '/address').read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

device_serial = 1
device_mac = getMAC('wlan0')
print(device_mac)

header = {'deviceIdentifier': device_serial, 'macAddress': device_mac}
print(header)
header_json = json.dumps(header)

rep_json = requests.post("http://espressotg.com/eotg/api/devices/registerDevice", data=header_json)
rep = rep_json.json()
print(rep)



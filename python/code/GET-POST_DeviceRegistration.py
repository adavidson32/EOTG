import requests
import json

device_serial = 1
device_mac = getMAC(wlan0)
print(device_mac)

header = {'deviceIdentifier': device_serial, 'macAddress': device_mac}
print(header)

reply = requests.post("http://espressotg.com/eotg/api/devices/registerDevice", json=header)
print(reply.text)
print(reply.json())

def getMAC(interface):
  try:
    str = open('/sys/class/net/' + str(interface) + '/address').read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

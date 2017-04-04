import requests
import urllib.parse
import urllib.request
import json

url_deviceRegistration = "http://espressotg.info/eotg/api/devices/registerDevice"

#-----------------------------------------------------------------------------------
def getMAC(interface):
  try:
    str = open('/sys/class/net/' + interface + '/address').read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  return cpuserial
#-----------------------------------------------------------------------------------

device_serial = getserial()
device_mac = getMAC('wlan0')
print("Device Serial Number: " + device_serial)
print("Device MAC Addr: " + device_mac)

header = {'deviceIdentifier': device_serial, 'macAddress': device_mac}
print("Header sent to Server: " + str(header))
data = urllib.parse.urlencode(header).encode()
response = urllib.request.urlopen(url_deviceRegistration, data)
body_json = response.read().decode()
body = json.loads(body_json)
print("Response from Server: " + str(body))
Device_ID = body['deviceId']
print("Assigned ID Number: " + str(Device_ID))

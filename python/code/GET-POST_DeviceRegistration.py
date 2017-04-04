import requests
import json

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

device_serial = getserial()
device_mac = getMAC('wlan0')
print("Device Serial Number: " + device_serial)
print("Device MAC Addr: " + device_mac)

header = {'deviceIdentifier': device_serial, 'macAddress': device_mac}
header_json = json.dumps(header)

rep_json = requests.post("http://espressotg.info/eotg/api/devices/registerDevice", data=header_json)
rep = rep_json.json()
rep_ID = rep['deviceId']
print(rep)
print(rep_ID)
print(type(rep_ID)



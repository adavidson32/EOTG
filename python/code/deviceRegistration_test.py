import requests
import json

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
print("device_serial file type: " + str(type(device_serial)))
print("device_mac file type: " + str(type(device_mac)))

header = {'@deviceIdentifier': device_serial, '@macAddress': device_mac}
header_json = json.dumps(header)
print(header)
print("Header Type: " + str(type(header)))
print(header_json)
print("Header_json Type: " + str(type(header_json)))
rep_json = requests.post("http://espressotg.info/eotg/api/devices/registerDevice", data=header_json)
print(rep_json)
rep = rep_json.json()
print(rep)
rep_ID = rep['deviceId']
print("Assigned ID Number: " + str(rep_ID))

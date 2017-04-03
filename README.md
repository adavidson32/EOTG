# Espresso-on-the-GO

## Github Contents:

### Python Programs: 
##### Project Code
- Read Sensor Values:
  - DS18B20
  - BMP280
  - MPU-6050
  - RC522
  - Averaging Functions for data
  - Data storage protocol for saving data to file periodically
- Communicate with NGINX Webserver
  - HTTP GET/PULL Requests
  - JSON Parser to decode info received from server
- Configure Wi-Fi + Bluetooth Networks
  - Code to add/remove/edit networks in wpa_supplicant file
  - Code to start hostapd software and configure new network (ssid, password, etc.)
  - Code to run BLE 4.0 Peripheral device w/ values for:
    - Brew ON/OFF Status
    - Current Brew Temperature
    - Current Device Battery Level
    - Current Device Water Level (or Empty/Not Empty...)
    - Wi-Fi Status + ability to receive ssid+password from phone via APP
  - Code to auto start hostapd network after ##sec. if no known network is found

##### Example Code
- Sensor Examples:
  - DS18B20
  - BMP280
  - MPU-6050
  - RC522
  - Averaging Functions for data
  - Data storage protocol for saving data to file (csv, txt, sqlite, etc...)
  

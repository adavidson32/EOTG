# Espresso-on-the-GO

## Github Contents:

### Python Programs: 
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
- Example Code:
  - For all sensors
  - MQTT use examples
  - General file operations
  - HTTP GET/PULL Requests + using JSON
  - Hosting HTTP Page on Pi
  - Running + Configuring hostapd network
  - BLE Peripheral/Master examples
  - RTC Use examples
  - Neopixel examples to get light patterns from
  - GUI + Inputs/Outputs Examples
  - Button reading w/ debounce parameters
  
  

import os, glob, time

class DS18B20:
   def __init__(self):
      # load required kernel modules
      os.system('modprobe w1-gpio')
      os.system('modprobe w1-therm')
      # Find file names for the sensor(s)
      base_dir = '/sys/bus/w1/devices/'
      device_folder = glob.glob(base_dir + '28*')
      self._num_devices = len(device_folder)
      self._device_file = list()
      i = 0
      while i < self._num_devices:
         self._device_file.append(device_folder[i] + '/w1_slave')
         i += 1

   def _read_temp(self,index):
      # Issue one read to one sensor
      # you should not call this directly
      f = open(self._device_file[index],'r')
      lines = f.readlines()
      f.close()
      return lines

   def tempC(self,index = 0):
      # call this to get the temperature in degrees C
      # detected by a sensor
      lines = self._read_temp(index)
      retries = 5
      while (lines[0].strip()[-3:] != 'YES') and (retries > 0):
         # read failed so try again
         time.sleep(0.1)
         #print('Read Failed', retries)
         lines = self._read_temp(index)
         retries -= 1

      if retries == 0:
         return 998

      equals_pos = lines[1].find('t=')
      if equals_pos != -1:
         temp = lines[1][equals_pos + 2:]
         return float(temp)/1000
      else:
         # error
         return 999

   def temp_all(self):
      temps = ()
      for i in range(device_count):
         temps += (tempC(i),)
      return temps

   def device_count(self):
      # call this to see how many sensors have been detected
      return self._num_devices

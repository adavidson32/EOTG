def states_brewing():
  device_state = 'Brewing'
  print("Brew Starting Now.....")
  print_state(device_state)
  time_heat_start = time.time()
  GPIO.output(relay_pin1, GPIO.LOW)
  GPIO.output(relay_pin2, GPIO.LOW)
  while (time.time() < (time_heat_start + brew_time)):
    time_pump_start = time.time()
    while (time.time() < (time_pump_start + 1)):
      coffee_temp = read_temp()
      lcd.lcd_display_string("Pump-ON Heat-ON", 1)
      lcd.lcd_display_string("Temp: {0:.1f}", 2)
      time.sleep(.1)
    GPIO.output(relay_pin2, GPIO.HIGH)
    time_pump_end = time.time()
    while (time.time() < (time_pump_end + 4)):
      coffee_temp = read_temp()
      lcd.lcd_display_string("Pump-OFF Heat-ON", 1)
      lcd.lcd_display_string("Temp: {0:.1f}", 2)
      time.sleep(.1)
    if (GPIO.input(button_pin)):
      button_state = buttonread()
      if button_state == 'HOLD':
        GPIO.output(relay_pin1, GPIO.HIGH)
        GPIO.output(relay_pin2, GPIO.HIGH)
        return "brew_cancelled"
  GPIO.output(relay_pin1, GPIO.HIGH)
  GPIO.output(relay_pin2, GPIO.HIGH)
  return "brew_success"
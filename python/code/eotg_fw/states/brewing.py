from ../io import relays

#update relevant variables / database variables
#new_state = Brewing
#turn on heater for X sec. and pump on with pwm cycle...

def start_brew():
    setup_pump_heater(input_variables)
    loop_exit = brew_loop(input_variables)
    exit_var = leave_brewing()
    return exit_var

def setup_pump_heater():

def brew_loop(input_variables):

def leave_brewing(cause)


#From 0412/main3....
#--------------------------------------------------------
def states_brewing():
  print("Brew Starting Now.....")
  time_start = time.time()
  pump.turn_on()
  heater.turn_on()
  while (time.time() < (time_start + brew_time)):
    coffee_temp = read_temp()
    print("Current coffee temmperature: {0:.1f} F".format(coffee_temp))
    if (GPIO.input(button_pin)):
      button_state = buttonread()
      if button_state == 'HOLD':
        GPIO.output(relay_pin1, GPIO.HIGH)
        GPIO.output(relay_pin2, GPIO.HIGH)
        return "brew_cancelled"
    time.sleep(1)
  GPIO.output(relay_pin1, GPIO.HIGH)
  GPIO.output(relay_pin2, GPIO.HIGH)
  return "brew_success"

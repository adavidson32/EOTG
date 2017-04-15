
def check_orientation():
  accel_data = mpu6050.get_accel_data()
  ax = float("{0:.3f}".format(accel_data['x']))
  ay = float("{0:.3f}".format(accel_data['y']))
  az = float("{0:.3f}".format(accel_data['z']))
  xz_fraction = math.fabs(ax / az)
  yz_fraction = math.fabs(ay / az)
  xz_angle = math.atan(xz_fraction)
  yz_angle = math.atan(yz_fraction)
  xz_angle = math.degrees(xz_angle)
  yz_angle = math.degrees(yz_angle)
  print("xz-angle: {0:.1f} deg.,  yz-angle: {1:.1f} deg.".format(xz_angle, yz_angle))
  if ((xz_angle <= 5) and (yz_angle <= 5)):
    return "level"
  elif ((xz_angle > 5) or (yz_angle  > 5)):
    return "not-level" 
 
def prebrew_check():
  check_level = check_orientation()
  if (ac == 'disconnected'):
    return 'ac_disconnected'
  elif (water_level == 'low'):
    return 'water_low'
  elif (check_level == 'not-level'):
    return 'not-level'
  else:
    return 'pass'

def states_waiting():
  device_state = 'Waiting'
  print("Device in waiting state")
  lcd.lcd_display_string("State: Waiting", 1)
  lcd.lcd_display_string("Profile #{}".format(profile_num), 2)
  but_func = buttonread()
  while (not(but_func == '2x Press') and not(but_func == '1x Press') and not(but_func == 'HOLD')):
    but_func = buttonread()
  if but_func == 'HOLD':
    print("Device turned off. Hold Button to turn back on....")
    states_background()
  elif but_func == "2x Press":
    test_results = prebrew_check()
    if (test_results == 'pass'):
      print("Brew Started")
      result = states_brewing()
      if result == "brew_success":
        print("Brew finished successfully and returned to waiting state")
      elif result == "brew_cancelled":
        print("Brew cancelled with 2x Press")
      else:
        print("Brew finished with error, returned to waiting state")
    elif but_func == "1x Press":
      profile_num = (profile_num + 1)%(number_profiles+1)
      print("Profile Changed to #{}....".format(profile_num))
    else:
      print("Error running brew. Check water level, device level, or AC connection...")
  states_waiting()
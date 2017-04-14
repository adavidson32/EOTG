def states_background():
  while 1:
    device_state = 'background'
    print("Device in Background State")
    print_state(device_state)
    but_func = buttonread()
    while not(but_func == 'HOLD'):
      but_func = buttonread()
    if (but_func == 'HOLD'):
      states_waiting()

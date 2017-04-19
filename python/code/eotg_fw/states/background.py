from ../neopixels import neopixels as np
from time import time


def background():
    background_init(input_variables)
    loop_exit = backgound_loop(input_variables)
    exit_var = exit_processing(loop_exit)
    if exit_var == 'hold_detected':
        run_waiting(exit_var)
    elif ((exit_var == '1x_detected') or (exit_var == '2x_detected')):
        display_battery()
    else:
        run_background


def backgound_init(input_variables):
    np_status = np.check_init()
    if np_status

def background_loop(input_variables):
    t_timeout = input_variables[4]
    t_loop_timeout = time() + t_timeout
    while time() < t_loop_timeout:
        button_status = check_button_events(t_last_check)


def check_button_events(t_last_check):
    #connect to eotg.db, find all


def display_battery():
    battery_level = ask_nano_batt()
    np.display(battery_level)
    return 'battery displayed'

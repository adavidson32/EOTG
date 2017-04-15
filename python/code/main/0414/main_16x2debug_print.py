import lcddriver


lcd = lcddriver.lcd()

def print16x2(func):
	if func == "welcome":
		lcd.lcd_display_string("Welcome to EOTG ", 1)
		lcd.lcd_display_string(" DEVICE STARTED ", 2)
	elif func == "ns_background":
		lcd.lcd_display_string("New State...    ", 1)
		lcd.lcd_display_string("S: Background   ", 2)
	elif func == "ns_waiting":
		lcd.lcd_display_string("New State...    ", 1)
		lcd.lcd_display_string("S: Waiting      ", 2)
	elif func == "ns_brewing":
		lcd.lcd_display_string("New State...    ", 1)
		lcd.lcd_display_string("S: Brewing      ", 2)
	elif func == "profile":
		lcd.lcd_display_string("New Profile...  ", 1)
		lcd.lcd_display_string("P: 1-Manual     ", 2)
	elif func == "not_level":
		lcd.lcd_display_string("Pre-Brew ERROR: ", 1)
		lcd.lcd_display_string("Device not Level", 2)
	elif func == " ":
		lcd.lcd_display_string(, 1)
		lcd.lcd_display_string(, 2)
	
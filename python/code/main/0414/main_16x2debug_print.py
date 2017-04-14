import lcddriver


lcd = lcddriver.lcd()

def print16x2(func):
	if func == "welcome":
		lcd.lcd_display_string("Welcome to EOTG ", 1)
		lcd.lcd_display_string(" DEVICE STARTED ", 2)
	elif func == "clear":
		lcd.lcd_display_string("                ", 1)
		lcd.lcd_display_string("                ", 2)
	elif func == "new_state":
		lcd.lcd_display_string("New State:      ", 1)
		lcd.lcd_display_string(lcd.lcd_display_string(str1, 2)
	elif func == " ":
		lcd.lcd_display_string(, 1)
		lcd.lcd_display_string(, 2)
	elif func == " ":
		lcd.lcd_display_string(, 1)
		lcd.lcd_display_string(, 2)
	elif func == " ":
		lcd.lcd_display_string(, 1)
		lcd.lcd_display_string(, 2)
	elif func == " ":
		lcd.lcd_display_string(, 1)
		lcd.lcd_display_string(, 2)
	elif func == " ":
		lcd.lcd_display_string(, 1)
		lcd.lcd_display_string(, 2)
	
    
def lcd_clear(lines):
	if lines == 1:
		lcd.lcd_display_string("                ", 1)
	elif lines == 2:
		lcd.lcd_display_string("                ", 2)
	else:
		lcd.lcd_display_string("                ", 1)
		lcd.lcd_display_string("                ", 2)
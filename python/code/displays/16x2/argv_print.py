import sys
import time
import lcddriver

lcd = lcddriver.lcd()

len_arg = len(sys.argv)
if len_arg==3:
  line1_text = sys.argv[1]
  line2_text = sys.argv[2]
else:
  print("No stings entered in argv[1] or argv[2]")
  line1_text = input("Enter text to display on Line #1 : ")
  line2_text = input("Enter text to display on Line #2 : ")
if ((len(line1_text) > 16) or (len(line2_text) > 16)):
  print("ERROR: Input string over 16 characters, can't print on one line")
  line1_text = input("Enter text to display on Line #1 : ")
  line2_text = input("Enter text to display on Line #2 : ")

to_add = 16-len(display_text)
for i in range(1, to_add):
  display_text += ' '

print('|{}|'.format(line1_text))
print('|{}|'.format(line2_text))

import sys
import time

len_arg = len(sys.argv)
if len_arg==3:
  display_text = sys.argv[1]
  line_num = int(sys.argv[2])
else:
  display_text = input("Enter text to display : ")
  line_num = int(input("Enter line to display text on (1 or 2) : "))
if (len(display_text) > 16):
  print("ERROR: Input string over 16 characters, can't print on one line")
  display_text = input("Enter a new string (under 16 characters) : ")
if not(line_num==1 or line_num==2):
  line_num = input("ERROR: invalid line number (Enter a line number as 1 or 2) : ")

to_add = 16-len(display_text)
for i in range(1, to_add):
  display_text += ' '
  
if (line_num==1):
  print('|{}| str_len = {}'.format(display_text, len(display_text)))
  print('|                | str_len = {}'.format((len('|                |')-2)))
elif (line_num==2):
  print('|                | str_len = {}'.format((len('|                |')-2)))
  print('|{}| str_len = {}'.format(display_text, len(display_text)))
  

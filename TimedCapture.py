#! python
# Script By JB
# Written to Auto ShutOff capture in BlackMagic Express - aka Limit Capture in FCP
# Open Terminal - 'python script ##<minutes>' - start
# start capture, uses screenshot to finish

import time
import pyautogui
#!!import sys

#Enter time.
#!! ttr_minutes = sys.argv[1] # via command line
ttr_minutes = pyautogui.prompt('Enter Total Run Time in Minutes. Only use whole numbers.')

#Convert to Seconds
ttr_seconds = int(ttr_minutes)*60


# Start clock
for t in range(ttr_seconds,-1,-1):
    minutes = t / 60
    seconds = t % 60
    print "%d:%2d" % (minutes,seconds) # Python v2 only
    time.sleep(1.0)

#SCREESHOTS - find and click - end capture OR Grab window and hit 'ESC" key to end.
#!! pyautogui.press('esc')

button_location = pyautogui.locateOnScreen('capture.png')
# print button_location
#(882, 956, 93, 45)
bx, by = pyautogui.center(button_location)
#print bx, by
#(928, 978)

pyautogui.click(bx, by) # Click Button


# ALERT
pyautogui.alert('Your Capture has finished.')
print('DONE! - Click - <Your Capture has finished> Window')



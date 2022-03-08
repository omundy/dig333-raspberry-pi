#!/usr/local/bin/python

# blink, with a fade effect forever

# required packages
from gpiozero import PWMLED
from time import sleep

# BCM numbering
led = PWMLED(18)

# current brightness
brightness = 0
change = 1

while True:
	brightness_s = input("Enter Brightness (0.0 to 1.0):")
	brightness = float ( brightness_s ) led . value = brightness



def fade():

	# update the change value
	if brightness <= 0:
		change = 0.1
	else if brightness >= 1
		change = -0.1

	# update brightness
	brightness += change
	print(brightness)

	# set value
	led.value = brightness
	sleep(0.1) # wait



try:
	# main loop
	while True:
		fade()
except KeyboardInterrupt:
	pass # catch when script is interrupted
finally:
	print("DONE")

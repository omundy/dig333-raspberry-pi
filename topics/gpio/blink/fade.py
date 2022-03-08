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

def fade():
	global brightness, change

	# update the change value
	if brightness <= 0:
		change = 0.1
		brightness = 0
	elif brightness >= 1:
		change = -0.1
		brightness = 1

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

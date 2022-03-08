#!/usr/local/bin/python

# blink, forever
# gpiozero version

# required packages
from gpiozero import LED
import time import sleep

# BCM numbering
led = LED(18)

def blink(pin):

	# turn the LED on
	print("ON")
	led.on()
	sleep(1.0) # wait

	# turn the LED off
	print("OFF")
	led.off()
	sleep(1.0) # wait


try:
	# main loop
	while True:
		blink(pin)
except KeyboardInterrupt:
	pass # catch when script is interrupted
finally:
	print("DONE")

#!/usr/local/bin/python

# blink, forever

# required packages
from gpiozero import LED
from time import sleep

# BCM numbering
led = LED(18)

while True:
	# turn the LED on
	print("ON")
	led.on()
	sleep(1.0) # wait

	# turn the LED off
	print("OFF")
	led.off()
	sleep(1.0) # wait

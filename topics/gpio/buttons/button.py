#!/usr/local/bin/python

# a basic button script

from gpiozero import Button
from time import sleep

button = Button(40)

def button():

	# if the button is pressed
	if button.is_pressed:
		return 1
	else:
		return 0

try:
	while True:
		print(button())	# print status of button
		time.sleep(.5) # pause between loops
except KeyboardInterrupt:
	pass # catch when script is interrupted
finally:
	print("DONE")

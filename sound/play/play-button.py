import RPi.GPIO as GPIO
import time, os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.IN)
input = GPIO.input(23)

while True:
	# PLAY SOUND
	if (GPIO.input(23) == False):
		os.system ("aplay ../example-sounds/darth_vader.wav")

GPIO.cleanup()

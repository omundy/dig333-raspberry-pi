import RPi.GPIO as GPIO
import time, os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.IN)
input = GPIO.input(23)

while True:
	# TAKE PICTURE
	if (GPIO.input(23) == False):
		print('taking photo')
		os.system('sudo python /home/pi/<path>/capture.py')
		print('uploading')
		os.system('sudo python /home/pi/<path>/upload.py')
		print('uploading finished')
		time.sleep(1)

GPIO.cleanup()

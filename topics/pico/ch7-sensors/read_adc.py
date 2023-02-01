
# Read a potentiometer or other anolog source
# POT center pin = GP26, outside pins connected to 3.3V and GND
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

from machine import ADC, Pin
import time

# ADC0 == GP26 so this could be written either way...
# adc = ADC(0) 
adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    time.sleep(1)
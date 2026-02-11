
# built-in LED blink
# Pi Pico W using CircuitPython

import time # type: ignore
import board # type: ignore
import digitalio # type: ignore

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT # set the direction of the pin

while True:
    led.value = True # turn the LED on
    print(1)
    time.sleep(0.5) # wait for 0.5 seconds
    led.value = False # turn the LED off
    print(0)
    time.sleep(0.5) # wait for 0.5 seconds
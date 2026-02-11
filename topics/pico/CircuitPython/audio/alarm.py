
# Cycle the frequency - Connect a buzzer to GP15 and ground
# https://docs.circuitpython.org/en/latest/shared-bindings/pwmio/
# Pi Pico W using CircuitPython

import time # type: ignore
import board # type: ignore
import digitalio # type: ignore
import pwmio # type: ignore

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT # set the direction of the pin

pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=440, variable_frequency=True)
pwm.duty_cycle = 2 ** 15  # Cycles the pin with 50% duty cycle (half of 2 ** 16) at 50hz

while True:
    led.value = True # turn the LED on
    pwm.frequency = 880
    time.sleep(0.2)
    led.value = False # turn the LED off
    pwm.frequency = 440
    time.sleep(0.1)



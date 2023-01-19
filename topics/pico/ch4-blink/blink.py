
# BLINK
import machine
import utime
# set onboard LED (pin 25) as OUT
# use "LED" with quotes instead of 25 on Pico W
led_pin = machine.Pin(25, machine.Pin.OUT)

while (True):
    # set on
    led_pin.value(1)
    utime.sleep(1)
    led_pin.value(0)
    utime.sleep(1)

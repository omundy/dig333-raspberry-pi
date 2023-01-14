
# BLINK
import machine
import utime
# set onboard LED as OUT
led_onboard = machine.Pin(25, machine.Pin.OUT)

while (True):
    # set on
    led_onboard.value(1)
    utime.sleep(1)
    led_onboard.value(0)
    utime.sleep(1)

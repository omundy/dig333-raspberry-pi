
# PWM pulse sine wave example
# https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html

from machine import Pin, PWM
import time, math

freq = 100
volume = 300

led = PWM(Pin(0))
led.freq(freq)

def pulse(l, t):
    for i in range(t):
        duty_cycle = int(math.sin(i / 10 * math.pi) * volume + volume)
        print(duty_cycle)
        l.duty_u16(duty_cycle)
        time.sleep_ms(t)
        
while True:
    pulse(led, 20)
    

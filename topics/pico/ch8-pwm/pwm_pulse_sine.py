
# https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html

from machine import Pin, PWM
import time, math

led = PWM(Pin(0))
led.freq(1500)
led.duty_u16(512)

def pulse(l, t):
    for i in range(20):
        duty_cycle = int(math.sin(i / 10 * math.pi) * 500 + 500)
        print(duty_cycle)
        l.duty_u16(duty_cycle)
        time.sleep_ms(t)
        
while True:
    pulse(led, 10)
    

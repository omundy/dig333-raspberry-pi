
# PWM pulse "up" example
# https://microcontrollerslab.com/raspberry-pi-pico-pwm-micropython-tutorial/
# https://randomnerdtutorials.com/esp32-esp8266-pwm-micropython/

from machine import Pin, PWM
from time import sleep

led = PWM(Pin(0))
led.freq(5000)

while True:
  for duty_cycle in range(0, 2048):
    led.duty_u16(duty_cycle)
    print(duty_cycle)
    sleep(0.001)
    


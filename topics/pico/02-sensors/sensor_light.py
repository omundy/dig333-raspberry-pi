
# Read a light sensor
# LDR connected to pin GP27 + ground

from machine import ADC, Pin
import time

adc = ADC(Pin(27))

while True:
    adc_value = adc.read_u16()
    print("adc_value   =", adc_value)
    adc_voltage = adc_value * (3.3 / (65535))
    print("adc_voltage = {}V ".format(adc_voltage))
    time.sleep_ms(500)

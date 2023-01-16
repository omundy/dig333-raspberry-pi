# read from a light sensor and log to the console
# plug an LDR into pins GP27 and ground
from machine import ADC
import time
adc = machine.ADC(27)
while True:
    adc_value = adc.read_u16()
    print("adc_value   =",adc_value)
    adc_voltage = adc_value * (3.3 / (65535))
    print("adc_voltage = {}V ".format(adc_voltage))
    time.sleep_ms(500)

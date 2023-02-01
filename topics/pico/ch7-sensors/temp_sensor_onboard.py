
# Read from onboard temp sensor
# https://electrocredible.com/raspberry-pi-pico-temperature-sensor-tutorial/

from machine import ADC
import time

adc = ADC(4) # note this connects directly to the temp sensor on the ADC channel 4, not a pin

while True:
    ADC_voltage = adc.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit = 32+(1.8*temperature_celcius)
    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))
    time.sleep_ms(500)

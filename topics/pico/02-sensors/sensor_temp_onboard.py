
# Read from onboard temp sensor
# https://electrocredible.com/raspberry-pi-pico-temperature-sensor-tutorial/

from machine import ADC
import time

# connects directly to the temp sensor on the ADC channel 4, not a pin
adc = ADC(4) 

while True:
    adc_value = adc.read_u16()
    # print("adc_value   =", adc_value)
    adc_voltage = adc_value * (3.3 / (65535))
    # print("adc_voltage = {}V ".format(adc_voltage))
    temperature_celcius = 27 - (adc_voltage - 0.706)/0.001721
    temp_fahrenheit = 32+(1.8*temperature_celcius)
    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))
    time.sleep_ms(500)

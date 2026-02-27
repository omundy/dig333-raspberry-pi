import board
import analogio
import time

# connect the piezo to ground and GP28. Place a 1M resistor between ground and GP28 (parallel to the piezo)

# Define the analog input pin
piezo_input = analogio.AnalogIn(board.GP28)

def get_voltage(pin):
    # read the 16-bit analog value and convert to a voltage (3.3V max)
    # The Pico's ADC is actually 12-bit, so this uses the full 16-bit range for scaling
    return pin.value * 3.3 / 65535

while True:
    # Read the raw analog value
    raw_value = piezo_input.value

    # You can also get the voltage reading if you prefer
    voltage = get_voltage(piezo_input)

    # Print the raw value (0-65535 range)
    print(f"raw_value:\t{raw_value} \tvoltage: {voltage}")

    # You will want to add logic here to interpret the value, e.g. a threshold trigger
    # if raw_value > 1000: # Example threshold
     #    print("Vibration detected!")

    time.sleep(0.1) # Small delay to avoid flooding the console

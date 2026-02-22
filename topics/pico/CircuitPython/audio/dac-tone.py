"""
CircuitPython I2S Tone playback example.
Plays a tone for one second on, one second off, in a loop.
https://docs.circuitpython.org/en/latest/shared-bindings/audiobusio/
"""

import time, array, math, audiocore, board, audiobusio

# GP > DAC (purple Amazon special) connections
i2s_bit_clock_pin   = board.GP16 # The bit clock (or serial clock) pin
i2s_word_select_pin = board.GP17 # The word select (or left/right clock) pin
i2s_data_pin        = board.GP18 # The data pin
# Board GND to DAC GND
# Board 3.3V to DAC VIN


audio = audiobusio.I2SOut(i2s_bit_clock_pin, i2s_word_select_pin, i2s_data_pin)

tone_volume = 0.05  # Increase this to increase the volume of the tone.
frequency = 440  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = array.array("h", [0] * length)

for i in range(length):
    sine_wave[i] = int((math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))
    
sine_wave_sample = audiocore.RawSample(sine_wave)

while True:
    audio.play(sine_wave_sample, loop=True)
    time.sleep(1)
    audio.stop()
    time.sleep(1)


# Synthio Demo
# https://learn.adafruit.com/audio-synthesis-with-circuitpython-synthio/simple-synthio-examples
# Pi Pico W using CircuitPython

import time # type: ignore
import board # type: ignore
import synthio # type: ignore
import audiomixer # type: ignore

# Initialize audio output (pins vary by board)
# for PWM audio with an RC filter
import audiopwmio # type: ignore
audio = audiopwmio.PWMAudioOut(board.GP15)

# Create a synthesizer object
synth = synthio.Synthesizer(sample_rate=44100)

# Start playing the synth
audio.play(synth)


# Play a note
# while True:
#     synth.press(65)  # midi note 65 = F4
#     time.sleep(0.5)
#     synth.release(65)  # release the note we pressed
#     time.sleep(2)

# Play a chord
while True:
    synth.press((65, 69, 72))  # midi note 65 = F4
    time.sleep(1)
    synth.release((65, 69, 72))  # release the note we pressed
    time.sleep(2)

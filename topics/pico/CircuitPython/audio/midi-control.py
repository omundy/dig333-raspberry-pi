import time
import board
import busio
import usb_midi

import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar

# Set USB MIDI up on channel 0
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0) # type: ignore

while True:
    # Send notes to computer
    midi.send(NoteOn(36, 100)) and midi.send(NoteOff(36, 0)) # type: ignore
    time.sleep(1)


# while True:
#     for i in range(40):
#         note = i + 50
#         # Send notes to computer
#         midi.send(NoteOn(note, 100)) and midi.send(NoteOff(note, 0)) # type: ignore
#         time.sleep(.125)
#         midi.send(NoteOn(note+3, 100)) and midi.send(NoteOff(note+3, 0)) # type: ignore
#         time.sleep(.125)
#         midi.send(NoteOn(note+5, 100)) and midi.send(NoteOff(note+5, 0)) # type: ignore
#         time.sleep(.25)
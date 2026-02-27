"""
# SPDX-FileCopyrightText: 2023 John Park and @todbot / Tod Kurt
# SPDX-License-Identifier: MIT
Detuning Oscillators for Fatter Sound
https://learn.adafruit.com/audio-synthesis-with-circuitpython-synthio/advanced-synthio-examples
"""

import digitalio, synthio, audiomixer
import time, array, math, audiocore, board, audiobusio, audiomixer
import ulab.numpy as np

# GP > DAC (purple Amazon special) connections
i2s_bit_clock_pin = board.GP16  # The bit clock (or serial clock) pin
i2s_word_select_pin = board.GP17  # The word select (or left/right clock) pin
i2s_data_pin = board.GP18  # The data pin
# Board GND to DAC GND
# Board 3.3V to DAC VIN


audio = audiobusio.I2SOut(i2s_bit_clock_pin, i2s_word_select_pin, i2s_data_pin)


mixer = audiomixer.Mixer(channel_count=1, sample_rate=44100, buffer_size=4096)

amp_env_slow = synthio.Envelope(attack_time=0.65, sustain_level=1.0, release_time=0.8)
synth = synthio.Synthesizer(channel_count=1, sample_rate=44100, envelope=amp_env_slow)

audio.play(mixer)
mixer.voice[0].play(synth)
mixer.voice[0].level = 0.3

# create sine, tri, saw & square single-cycle waveforms to act as oscillators
SAMPLE_SIZE = 512
SAMPLE_VOLUME = 32000  # 0-32767
half_period = SAMPLE_SIZE // 2
wave_sine = np.array(
    np.sin(np.linspace(0, 2 * np.pi, SAMPLE_SIZE, endpoint=False)) * SAMPLE_VOLUME, # type: ignore
    dtype=np.int16,
)
wave_saw = np.linspace(SAMPLE_VOLUME, -SAMPLE_VOLUME, num=SAMPLE_SIZE, dtype=np.int16)
wave_tri = np.concatenate(
    (
        np.linspace(-SAMPLE_VOLUME, SAMPLE_VOLUME, num=half_period, dtype=np.int16),
        np.linspace(SAMPLE_VOLUME, -SAMPLE_VOLUME, num=half_period, dtype=np.int16),
    ) # type: ignore
)
wave_square = np.concatenate(
    (
        np.full(half_period, SAMPLE_VOLUME, dtype=np.int16),
        np.full(half_period, -SAMPLE_VOLUME, dtype=np.int16),
    ) # type: ignore
)


# note1 = synthio.Note( frequency = 220, waveform = wave_sine, amplitude=0.3)

detune = 0.003  # how much to detune
num_oscs = 1
midi_note = 52

while True:
    print("num_oscs:", num_oscs)
    notes = []  # holds note objs being pressed
    # simple detune, always detunes up
    for i in range(num_oscs):
        f = synthio.midi_to_hz(midi_note) * (1 + i * detune)
        notes.append(synthio.Note(frequency=f, waveform=wave_saw))
    synth.press(notes)
    time.sleep(3.6)
    synth.release(notes)
    time.sleep(0.1)
    # increment number of detuned oscillators
    num_oscs = num_oscs + 1 if num_oscs < 5 else 1


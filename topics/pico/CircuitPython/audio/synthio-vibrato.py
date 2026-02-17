# https://github.com/todbot/circuitpython-synthio-tricks?tab=readme-ov-file#vibrato-pitch-bend-with-lfo

import board, time, audiopwmio, synthio
audio = audiopwmio.PWMAudioOut(board.GP15)
synth = synthio.Synthesizer(sample_rate=22050)
audio.play(synth)

lfo = synthio.LFO(rate=5, scale=0.1)  # 5 Hz lfo at 0.5%

while True:
    midi_note = 65
    note = synthio.Note( synthio.midi_to_hz(midi_note), bend=lfo ) # type: ignore
    synth.press(note)
    time.sleep(1.0)
    synth.release(note)
    time.sleep(1.0)
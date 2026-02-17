# https://github.com/todbot/circuitpython-synthio-tricks?tab=readme-ov-file#tremolo-volume-change-with-lfo

import board, time, audiopwmio, synthio
audio = audiopwmio.PWMAudioOut(board.GP15)
synth = synthio.Synthesizer(sample_rate=22050)
audio.play(synth)

lfo_tremo1 = synthio.LFO(rate=3)  # 3 Hz for fastest note
lfo_tremo2 = synthio.LFO(rate=2)  # 2 Hz for middle note
lfo_tremo3 = synthio.LFO(rate=1)  # 1 Hz for lower note
lfo_tremo4 = synthio.LFO(rate=0.75) # 0.75 Hz for lowest bass note

midi_note = 65
note1 = synthio.Note( synthio.midi_to_hz(midi_note), amplitude=lfo_tremo1) # type: ignore
note2 = synthio.Note( synthio.midi_to_hz(midi_note-7), amplitude=lfo_tremo2) # type: ignore
note3 = synthio.Note( synthio.midi_to_hz(midi_note-12), amplitude=lfo_tremo3) # type: ignore
note4 = synthio.Note( synthio.midi_to_hz(midi_note-24), amplitude=lfo_tremo4) # type: ignore
synth.press( (note1, note2, note3, note4) )

while True:
    print("hi, we're just groovin")
    time.sleep(1)
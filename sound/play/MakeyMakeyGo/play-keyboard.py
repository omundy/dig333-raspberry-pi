#!/usr/bin/python

# Play sound from keyboard input
# - Example from MakeyMakeyGo
# - uses Tkinter so you should run it from a GUI# 

import Tkinter as tk
from subprocess import call

def onKeyPress(event):
    text.insert('end', "\nYou pressed %s" % (event.char, ))
    if (event.char == "A"):
        call(["afplay", "meow.mp3"])

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Arial', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()

#!/usr/bin/python

# capture.py
# Capture an image with libcamera
# 2022 Owen Mundy owenmundy.com

import os

cmd = 'libcamera-still -o hello.jpg'

os.system(cmd)

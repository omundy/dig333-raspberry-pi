#!/usr/bin/python

# capture.py
# Capture an image with raspistill
# 2013 Owen Mundy owenmundy.com
# sudo crontab -e
#    */10 * * * * python /home/pi/<path>raspistill/capture.py


import time
import os

cmd = 'raspistill -n -t 2000 -o /home/pi/p_'
cmd += time.strftime("%Y%m%d_%H%M%S") + '.jpg'

os.system(cmd)

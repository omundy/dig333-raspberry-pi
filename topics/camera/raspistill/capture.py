#!/usr/bin/python

# capture.py
# Capture an image with raspistill
# 2013 Owen Mundy owenmundy.com
# sudo crontab -e
#    */10 * * * * python /home/pi/<path>raspistill/capture.py


import time,os

cmd = 'raspistill -n -t 2000'
cmd += time.strftime(" -o /home/pi/<path>/images/p_%Y%m%d_%H%M%S") +'.jpg'

os.system(cmd)


'''

#OLD ONE - WAS HANGING...

import time,subprocess

# raspistill to capture, -n (no preview), -t (timeout=2000ms), -o (full path)
cmd = 'raspistill -n -t 2000'
cmd += time.strftime(" -o /home/pi/<path>/images/p_%Y%m%d_%H%M%S") +'.jpg'

# start process
cam = subprocess.Popen(cmd, shell=True)

# need to wait for image to process
time.sleep(5)

# we have to kill the process in order for it to stop
kill = 'kill -9 '+ str(cam.pid)
subprocess.Popen(kill, shell=True)
'''

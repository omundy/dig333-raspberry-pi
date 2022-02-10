#!/usr/bin/python

# capture.py
# Capture an image with fswebcam
# 2013 Owen Mundy owenmundy.com
# used with fablab_robomonitor
# crontab -e
#    */10 * * * * python /home/pi/<path>/capture.py

import time,subprocess

# first export the library path
#cmd  = 'export LD_LIBRARY_PATH=.'
#export = subprocess.Popen(cmd, shell=True)

cmd  = 'fswebcam -r 960x720 -d /dev/video0 -i 0 --jpeg 80 '
cmd += '--title "fablab_robomonitor" --font "arial:10" '
cmd += '--line-colour "#FF000000" --banner-colour "#AA000000" '
cmd += time.strftime("~/<path>/images/p_%Y%m%d_%H%M%S") +'.jpg'

#fswebcam -r 960x720 -d /dev/video2 --jpeg 80 --title "fablab_robomonitor" --line-colour "#FF000000" --banner-colour "#AA000000" --font "arial:10" ~/fswebcam/images/p_20130413_103003.jpg

# start process
cam = subprocess.Popen(cmd, shell=True)

# need to wait for image to process
time.sleep(7)

# we have to kill the process in order for it to stop
kill = 'kill -9 '+ str(cam.pid)
subprocess.Popen(kill, shell=True)

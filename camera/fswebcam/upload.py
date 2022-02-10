#!/usr/bin/python

# upload.py
# Upload most recent file created in a directory
# used with fablab_robomonitor
# 2013 Owen Mundy owenmundy.com
# crontab -e
#    */10 * * * * python /home/pi/<path>/upload.py

import ftplib, os, time
dir='/home/pi/<path>/images/'

# return newest file
def newestfile(dir,pre):
	files = sorted([ f for f in os.listdir(dir) if f.startswith(pre)])
	uploadfile = files[-1]
	return uploadfile

uploadfile = newestfile(dir,'p_')

#upload a text or binary file
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(dir + file, "rb"), 1024)
        ftp.storbinary("STOR " + "p_000_current.jpg", open(dir + file, "rb"), 1024)

ftp = ftplib.FTP("<domain>")
ftp.login("<user>", "<pass>")
ftp.cwd('<directory>') # change working directory
upload(ftp, uploadfile) # upload text or binary file

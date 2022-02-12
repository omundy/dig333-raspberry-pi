#!/usr/bin/python

# upload.py
# Upload most recent file created in a directory
# 2013 Owen Mundy owenmundy.com
# used with fablab_robomonitor
# sudo crontab -e
#    */10 * * * * python /home/pi/<path>/upload.py
#
# NOTE: Make sure you chown on the server so your FTP user has permission to upload

#### NOTE TO SELF. ALL THIS CODE WORKS, BUT DON'T NEED SO IT IS COMMENTED OUT.

import pysftp, sys, os, time
localdir='/home/pi/<path>/images/'
remotedir='./fablab.art.fsu.edu/web/robomonitor2/'

'''
# return newest file
def newestfile(localdir,pre):
	files = sorted([ f for f in os.listdir(localdir) if f.startswith(pre)])
	uploadfile = files[-1]
	return uploadfile

# file to upload
uploadfile = newestfile(localdir,'p_')
'''

# create connection
srv = pysftp.Connection(host="<domain>", username="<user>",password="<pass>")

# upload file twice, one for current copy, one for history
srv.put(localdir + "p_000_current.jpg", remotedir + "p_000_current.jpg")
#srv.put(localdir + uploadfile, remotedir + uploadfile)

'''
# remove local file (so the HD doesn't overfill and cause the system to stop working)
cmd = 'rm ' + localdir + './*'
os.system(cmd)
'''

← [Raspberry Pi](../../README.md)

<a href="../../README.md"><img width="150" src="../../assets/img/RPi-Logo-Reg-SCREEN.webp"></a>

# Raspberry Pi + Video









## Video Looping


Quicktime and VLC provide easy ways (and a GUI) to playback looping video. These scripts use OMX Player to do the same.


### Raspberry Pi Video Looper

This disk image contains a bash script that automatically play and loop full-screen videos as an "exhibition kiosk".

- [Setup instructions and notes](https://www.timschwartz.org/raspberry-pi-video-looper/)
- [Video Looper bash script](https://github.com/timatron/videolooper-raspbian) by [Tim Schwartz](http://www.timschwartz.org)


### loop_pi_video.sh

This [script](https://gist.github.com/cpmpercussion/607e7fd5ad1f5b1cf4fc76950e6bcd13) plays a video in an infinite loop on a raspberry pi for a video-art exhibition. It was written for a video in portrait orientation so the video is rotated 270 to use up the whole screen (which was also rotated). Charles Martin, July 2016

```bash
#!/bin/bash

omxplayer -o local --loop /home/pi/video.mp4 --orientation 270
```

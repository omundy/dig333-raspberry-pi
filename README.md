

# Raspberry Pi

A collection of [documentation](topics/docs) and [scripts](topics) (bash | python) for the Raspberry Pi:

- [Introduction](topics/introduction)
- [GPIO](topics/gpio)
- [Camera](topics/camera)
- [Networks](topics/networks)
- [Sensors](topics/sensors)
- [Server](topics/server)
- [Sound](topics/sound)
- [Time](topics/time)
- [Video](topics/video)
- [Networks](topics/networks)












## Software


### Install Chrome

For example, exhibiting projects with a web browser [reference](https://raspberrypi.stackexchange.com/questions/374/how-do-i-install-google-chrome)

```bash
# update
sudo apt-get update
# install browser
sudo apt-get install chromium-browser
```


### Run Chrome full-screen

Start Chromium fullscreen from the command line [reference](https://askubuntu.com/a/687870/372666)

```bash
chromium-browser --app=http://example.com --start-fullscreen
```


### Start Chrome full-screen script

From [tally-monsters / exhibitpi2019 ](https://github.com/sneakaway-studio/tally-monsters/tree/main/platforms/raspberry-pi)

1. Copy the file `start-full-screen.sh` (below) to the Pi desktop
2. Make it executable `chmod +x start-full-screen.sh`
3. Edit the url per your application
4. Double click or run it in the terminal (not over SSH) `./start-full-screen.sh`

```bash
#!/bin/bash

chromium-browser --app=http://localhost/tally-monsters/loop.html --start-fullscreen --noerrdialogs --disable-infobars
```

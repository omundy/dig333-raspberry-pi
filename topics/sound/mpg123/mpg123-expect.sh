#!/usr/bin/expect -f

# Use expect to stream audio
#######################################
# Expect is a program that "talks" to other interactive programs according to a script.
# https://linux.die.net/man/1/expect
# https://likegeeks.com/expect-command/
# https://www.thegeekstuff.com/2010/10/expect-examples/

# 1. Install Expect
# ... on Mac w/Homebrew
# brew install expect
# ... or on Raspberry Pi
# apt-get install expect -y

# 2. Point to the installation. Run:
# which expect
# Then edit the path in the shebang in this file (at the top)

# 3. Make it executable
# chmod +x ./play-expect.sh


# run forever
# set timeout -1

# spawn the program
spawn mpg123 -R
expect "@R MPG123 (ThOr) v9\r"

# start sending commands
send -- "SILENCE\r"
expect "@silence\r"
send -- "LOAD http://streamer.radio.co/s7de3f3534/listen\r"
expect "\r"

# expect is an extension of the tcl language
# http://tcl.tk/man/tcl8.5/TclCmd/for.htm
for {set x 0} {$x<10} {incr x} {
	# switch back and forth between two different EQ files
	send -- "EQFILE ./eq-files/eq-left.txt\r"
    expect "\r"
    sleep 2
    send -- "EQFILE ./eq-files/eq-right.txt\r"
    expect "\r"
    sleep 2
}


# close

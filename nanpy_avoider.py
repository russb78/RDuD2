#!/usr/bin/env python
# Avoider sketch for Nanpy-controlled frindo bot
# Russell Barnes - 02 Oct 2013
from nanpy import Arduino
from time import sleep

from motorfuncs import *
from sensorfuncs import *

lock = 5

Arduino.pinMode(lock, Arduino.INPUT)

def debug():
"""
If lock switch is in the locked position stop motors and give sensor feedback
"""
    stop()
    reading = read_sensors()
    Arduino.delay(5)
    if reading[0] > frontTrigger:
        print "Front bump detected!"
    elif reading[1] > sideTrigger:
        print "Right bump detected!"
    elif reading[2] > sideTrigger:
        print "Left bump detected!"
    elif reading[3] > rearTrigger:
        print "Rear bump detected!"
    else:
        print "Front:", reading[0], " | Right:", reading[1], " | Left:", reading[2], " | Rear:", reading[3]
        sleep(0.1)

def main():
    while True:
        try:
            locked = Arduino.digitalRead(lock)
            if locked == 0:
                debug()
            else:
                if not front_bump():
                    go(100)
                else:
                    ### Avoider coder starts below ###
                    stop()
                    reading = read_sensors()
                    print reading
                    ### Avoider code ends above ###
        except KeyboardInterrupt:
            close_pins()0
            print "\nExiting"
            quit()

if __name__ == '__main__':
    main()
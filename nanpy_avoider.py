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
If lock switch is in the locked position stop motors and give sensor feedback instead
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
                ### Actual Avoider coder starts below ###
                if not front_bump():
                    if not left_bump() and not right_bump():
                        print "No bump detected - on we go!"
                        go(200)
                        if left_bump() and not right_bump():
                            print "Left bump detected... Turning right"
                            rot_cw(100, 200)
                        elif right_bump() and not left_bump():
                            print "Right bump detected... Turning left"
                            rot_ccw(100, 200)
                        elif left_bump() and right_bump():
                            print "Both left & right bumps detected... Turning round!"
                            rot_cw(500, 200)
                else:
                    print "Front bump detected... Turning round!"
                    rot_cw(500, 200)
                # avoider code ends above
        except KeyboardInterrupt:
            close_pins()
            print "\nExiting"
            quit()


if __name__ == '__main__':
    main()

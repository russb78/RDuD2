#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  controlfuncs.py
#  
#  Copyright 2013 Russell Barnes
#  

def map(x, in_min, in_max, out_min, out_max):
    """
    Arduino-style map function to take input min/max and apply to 
    output min/max.
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def degrees(x): ### Tweak specifically for you own robot with testing ###
    """
    x is the number of degrees you with the robot to spin on the spot.
    0 == none - 259 == a full 360 degree spin. X is the Arduino.delay length
    """
    return (x - 0) * (1021 - 0) / (359 - 0) + 0

def pan_angle(x)
    """
    Pan servo range should be constrain between 0-149
    (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    """
    return (x - 0) * (149 - 0) / (179 - 0) + 0

def tilt_angle(x)
    """
    Tilt servo range should be constrained between 50-179
    (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    """
    return (x - 0) * (179 - 50) / (179 - 0) + 50

def close_pins():
    """
    Close all motor pins to quit cleanly upon end or exception
    """
    Arduino.analogWrite(speedA, Arduino.LOW)
    Arduino.analogWrite(speedB, Arduino.LOW)
    Arduino.digitalWrite(dirA, Arduino.LOW)
    Arduino.digitalWrite(dirB,Arduino.LOW)

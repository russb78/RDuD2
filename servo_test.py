#!/usr/bin/env python

# Servo sketch for Nanpy-controlled frindo bot
# Russell Barnes - 09 Oct 2013

# tilt range contrain between 50-179
# pan central position = 70 (constrain between 20-159)?

from nanpy import Arduino
from nanpy import Servo
from motorfuncs import *
from sensorfuncs import *
from time import sleep

pan_servo = Servo(2)
tilt_servo = Servo(3)

"""
pan_pos = pan_servo.read()
tilt_pos = tilt_servo.read()
"""

### CONSTANTS ###
low_tilt = 50 # lowest position
home_tilt = 90 # home position (middle)
high_tilt = 179 # highest position

right_pan = 0 # (from behind)
right_half = 30
home_pan = 70 # home (middle)
left_half = 110
left_pan = 149 #  (from behind)

def set_home():
    pan_servo.write(home_pan)
    tilt_servo.write(home_tilt)

def get_pan():
    return pan_servo.read()
    
def get_tilt():
    return tilt_servo.read()

def set_pan(x):
    pan_servo.write(x)
    
def set_tilt(x):
    tilt.servo.write(x)

def pan_right():
    next_pos = get_pan() - 2
    pan_servo.write(next_pos)
    if get_pan() > right_pan:
        pan_right()

def pan_left():
    next_pos = get_pan() + 2
    pan_servo.write(next_pos)
    if get_pan() < left_pan:
        pan_left()

def tilt_up():
    next_pos = get_tilt() + 2
    tilt_servo.write(next_pos)
    if get_tilt() < tilt_high:
        tilt_up()
        
def tilt_down():
    next_pos = get_tilt() - 2
    tilt_servo.write(next_pos)
    if get_tilt() > tilt_low:
        tilt_up()

#########

try:
    pan_right()
    sleep(0.5)
    pan_left()
    sleep(0.5)
    set_home()
except KeyboardInterrupt:
    quit()

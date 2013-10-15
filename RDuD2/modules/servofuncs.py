#!/usr/bin/env python

# Servo sketch for Nanpy-controlled frindo bot
# Russell Barnes - 09 Oct 2013

from nanpy import Arduino
from nanpy import Servo
from time import sleep

pan_servo = Servo(2) # pan servo is on digital pin 2
tilt_servo = Servo(3) # tilt servo is on digital pin 3

# Enter debug mode to quickly test servo functions
DEBUG = False

### CONSTANTS ###

# tilt range contrain between 50-179
low_tilt = 50 # lowest position
home_tilt = 90 # home position (middle)
high_tilt = 179 # highest position

# pan central position = 70 (constrain between 0-149)
right_pan = 0 # (from behind)
half_right = 30
home_pan = 70 # home (middle)
half_left = 110
left_pan = 149 #  (from behind)

####

def set_home():
    """Puts the pan and tilt in its standard home position"""
    pan_servo.write(home_pan)
    tilt_servo.write(home_tilt)

def get_pan():
    """ returns the current pan servo position"""
    return pan_servo.read()
    
def get_tilt():
    """ returns the current tilt servo position"""
    return tilt_servo.read()

def set_pan(position):
    """ sets the pan servo position directly """
    pan_servo.write(position)
    
def set_tilt(position):
    """ sets the tilt servo position directly """
    tilt_servo.write(position)

def pan_right():
    """ Asks the pan servo to pan full right """
    next_pos = get_pan() - 2
    pan_servo.write(next_pos)
    if get_pan() > right_pan:
        pan_right()

def pan_left():
    """ Asks the pan servo to pan full left """
    next_pos = get_pan() + 2
    pan_servo.write(next_pos)
    if get_pan() < left_pan:
        pan_left()

def tilt_up():
    """ Asks the tilt servo to tilt up fully """
    next_pos = get_tilt() + 2
    tilt_servo.write(next_pos)
    if get_tilt() < tilt_high:
        tilt_up()
        
def tilt_down():
    """ Asks the tilt servo to tilt down fully """
    next_pos = get_tilt() - 2
    tilt_servo.write(next_pos)
    if get_tilt() > tilt_low:
        tilt_down()

#########

if DEBUG:
    try:
        set_home()
        sleep(0.5)
        set_tilt(low_tilt)
        sleep(1)
        set_pan(half_right)
        sleep(0.7)
        set_pan(half_left)
        sleep(0.7)
        set_pan(half_right)
        sleep(0.7)
        set_pan(half_left)
        sleep(0.7)
        set_home()
    except KeyboardInterrupt:
        quit()

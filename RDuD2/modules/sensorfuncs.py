#!/usr/bin/env python
# Sensor control for Nanpy-controlled frindo bot
# Russell Barnes - 02 Oct 2013

from nanpy import Arduino

# define the analog pins used by the IR sensors
FrontBump = 0   # Front IR sensor connected to pin 0
RightBump = 1   # Right-hand IR sensor (as viewed from rear) connected to pin 1
LeftBump = 2    # Left-hand IR sensor (as viewed from rear) connected to pin 2
RearBump = 3    # Rear IR sensor connected to pin 4

# assing the pins as inputs
for pins in (FrontBump, RightBump, LeftBump,RearBump):
    Arduino.pinMode(pins, Arduino.INPUT)

# define the threshold at which bump events are detected 
frontTrigger = 300
sideTrigger = 300
rearTrigger = 300

#print sensor readings while true
DEBUG = False

def front_bump():   # check for bump, if bump detected return 1
    bump = Arduino.analogRead(FrontBump)
    if bump > frontTrigger:
        return True
    else:
        return False

def right_bump():
    bump = Arduino.analogRead(RightBump)
    if bump > sideTrigger:
        return True
    else:
        return False
    
def left_bump():
    bump = Arduino.analogRead(LeftBump)
    if bump > sideTrigger:
        return True
    else:
        return False
    
def rear_bump():
    bump = Arduino.analogRead(RearBump)
    if bump > rearTrigger:
        return True
    else:
        return False
    
def read_sensors():
    """
    Reads each of the Sharp sensors are returns a list of analog readings
    in order: front, right, left, rear
    """
    reading = []
    for i in [FrontBump, RightBump, LeftBump, RearBump]:
        reading.append(Arduino.analogRead(i))
        Arduino.delay(1)
    return reading

while DEBUG: #for sensor debugging purposes only
    reading = read_sensors()
    Arduino.delay(1)
    print "Front:", reading[0], " | Right:", reading[1], " | Left:", reading[2], " | Rear:", reading[3]

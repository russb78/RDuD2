#!/usr/bin/env python
# Motor control for Nanpy-controlled frindo bot
# Russell Barnes - 02 Oct 2013

from nanpy import Arduino

# set RobotShield pins for motors
speedA = 6
speedB = 9 # b is the left hand motor (according to the RobotShield)
dirA = 8
dirB = 7

#set the motor pins as outputs
for pins in (dirA, dirB, speedA, speedB):
    Arduino.pinMode(pins, Arduino.OUTPUT)

### Core motor functions ###

def stop():
    """
    Simply stops your robot
    """
    Arduino.analogWrite(speedA, Arduino.LOW)
    Arduino.analogWrite(speedB, Arduino.LOW)

def forward(dist, vel):
    """
    Move forward for dist (time) at vel (motor speed)
    """
    Arduino.digitalWrite(dirA, Arduino.HIGH)
    Arduino.digitalWrite(dirB, Arduino.HIGH)
    Arduino.analogWrite(speedA, vel)
    Arduino.analogWrite(speedB, vel)
    Arduino.delay(dist)

def reverse(dist, vel):
    """
    Move backwards for dist (time) at vel (motor speed)
    """
    Arduino.digitalWrite(dirA, Arduino.LOW)
    Arduino.digitalWrite(dirB, Arduino.LOW)
    Arduino.analogWrite(speedA, vel)
    Arduino.analogWrite(speedB, vel)
    Arduino.delay(dist)

def rot_cw(angle, vel):
    """
    Turns to the right according to angle (delay)
    """
    Arduino.digitalWrite(dirA, Arduino.LOW)
    Arduino.digitalWrite(dirB, Arduino.HIGH)
    Arduino.analogWrite(speedA, vel)
    Arduino.analogWrite(speedB, vel)
    Arduino.delay(angle)

def rot_ccw(angle, vel):
    """
    Spins to the left according to angle (delay),
    then stops the motors
    """
    Arduino.digitalWrite(dirA, Arduino.HIGH)
    Arduino.digitalWrite(dirB, Arduino.LOW)
    Arduino.analogWrite(speedA, vel)
    Arduino.analogWrite(speedB, vel)
    Arduino.delay(angle)

def turn_right(angle, vel):
    """
    Turns to the right according to angle (delay)
    """
    Arduino.digitalWrite(dirA, Arduino.LOW)
    Arduino.digitalWrite(dirB, Arduino.HIGH)
    Arduino.analogWrite(speedA, Arduino.LOW)
    Arduino.analogWrite(speedB, vel)
    Arduino.delay(angle)

def turn_left(angle, vel):
    """
    Turns to the left according to angle (delay)
    """
    Arduino.digitalWrite(dirA, Arduino.HIGH)
    Arduino.digitalWrite(dirB, Arduino.LOW)
    Arduino.analogWrite(speedA, vel)
    Arduino.analogWrite(speedB, Arduino.LOW)
    Arduino.delay(angle)

def go(vel):
    """
    Start the motors and keep them running until told otherwise
    """
    Arduino.digitalWrite(dirA, Arduino.HIGH)
    Arduino.digitalWrite(dirB, Arduino.HIGH)
    Arduino.analogWrite(speedA, vel)
    Arduino.analogWrite(speedB, vel)

#!/usr/bin/env python3

from time import sleep
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent
from ev3dev2.sound import Sound

ir = InfraredSensor()
# ir.on_channel1_top_left = top_left_channel_1_action

motor_a = LargeMotor(OUTPUT_A)

# def top_left_channel_1_action(state):
#     print("top left on channel 1: %s" % state)

def turn_left(state):
    if state:
        motor_a.on(SpeedPercent(-30))
    else:
        motor_a.stop()

def turn_right(state):
    if state:
        motor_a.on(SpeedPercent(30))
    else:
        motor_a.stop()

ir.on_channel4_bottom_left = turn_left
ir.on_channel4_bottom_right = turn_right

spkr = Sound()
spkr.speak('Infrared is ready!')

while True:
    ir.process()
    sleep(0.01)

#!/usr/bin/env python3

# Elevator test
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sound import Sound

spkr = Sound()

spkr.speak('Elevator is ready!')
# m = MoveTank(OUTPUT_A, OUTPUT_B)
m1 = LargeMotor(OUTPUT_A)
# m2 = LargeMotor(OUTPUT_B)
ts = TouchSensor()
leds = Leds()
# Initialize button handler
button = Button()

# print("Press the touch sensor to change the LED color!")

while True:
    if button.left:
        m1.on_for_rotations(SpeedPercent(30), 2)
        # spkr.play_file('elevator-ding-sound.wav')
    if button.right:
        m1.on_for_rotations(SpeedPercent(30), -2)
        # spkr.play_file('elevator-ding-sound.wav')
    if button.up:
        m1.on_for_rotations(SpeedPercent(30), 1)
        # spkr.play_file('elevator-ding-sound.wav')
    if button.down:
        m1.on_for_rotations(SpeedPercent(30), -1)
        # spkr.play_file('elevator-ding-sound.wav')
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
        # spkr.play_file('explode.wav')
        # m.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 0.25)
    # else:
    #     leds.set_color("LEFT", "RED")
    #     leds.set_color("RIGHT", "RED")
    # # don't let this loop use 100% CPU
    sleep(0.01)

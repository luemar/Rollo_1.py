#!/usr/bin/python3
import logging
from signal import pause
from time import sleep
from gpiozero import Button, DigitalOutputDevice


button = Button(12, pull_up=False)

while True:
    if button.is_pressed:
        print('pressed')
    else:
        print('not pressed')
    sleep(2)

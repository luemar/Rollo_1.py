#!/usr/bin/python3
import logging
from signal import pause

from gpiozero import Button, DigitalOutputDevice

LINKS_ZU_PIN = 27
MOTOR_PIN_LINKS = 25


def main():
    rechts_man_auf = Button(LINKS_ZU_PIN)
    
    motor_rechts_auf = DigitalOutputDevice(MOTOR_PIN_LINKS)
  
    rechts_man_auf.when_pressed = motor_rechts_auf.on
    rechts_man_auf.when_released = motor_rechts_auf.off

    pause()


if __name__ == "__main__":
    main()

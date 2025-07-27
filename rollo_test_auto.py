#!/usr/bin/python3
import logging
from signal import pause
from time import sleep  # Add this import
from gpiozero import Button, DigitalOutputDevice

rechts_auto_auf = Button(17, hold_time=1)
motor_re_auf = DigitalOutputDevice(25)

def automatisch_fahren_li():  # Remove the motor parameter
    motor_re_auf.on()  # Use the global motor_li_auf directly
    sleep(17.5)
    motor_re_auf.off()
    print('rollo li automatisch gefahren')
    logging.info('rollo li automatisch gefahren')

def main():
    rechts_auto_auf.when_held = automatisch_fahren_li  # Assign function directly, no tuple
    pause()

if __name__ == "__main__":
    main()

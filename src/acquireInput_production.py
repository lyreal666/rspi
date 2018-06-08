#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import threading
import RPi.GPIO as GPIO
import time
from enum import Enum, unique
from src.globalVariables import GREEN, YELLOW

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''

'''


@unique
class LEDMode(Enum):
    ALWAYS = 0
    BLINK = 1
    OFF = 2
    SOME = 3


def blink(port, duration=0.5):
    while True:
        GPIO.output(port, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(port, GPIO.LOW)
        time.sleep(duration)


def light(port, duration):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(port, GPIO.LOW)


def ctrlLED(port, mode, light_duration=3, blink_duration=0.5):
    if mode == LEDMode.ALWAYS:
        GPIO.output(port, GPIO.HIGH)
    elif mode == LEDMode.BLINK:
        t = threading.Thread(target=blink, args=(port, blink_duration), name=f"Blink_LED_{port}")
        t.start()
    elif mode == LEDMode.OFF:
        GPIO.output(port, GPIO.LOW)
    elif mode == LEDMode.SOME:
        t = threading.Thread(target=light, args=(port, light_duration), name=f"Blink_LED_{port}")
        t.start()


def acquire(instructions):
    while True:
        instruction = input("输入命令: ")
        if instruction.strip() == "":
            ctrlLED(YELLOW, LEDMode.ALWAYS)
            instructions["RECD2PLAY"]()
            ctrlLED(YELLOW, LEDMode.OFF)
        elif instruction.lower().strip() == "q":
            ctrlLED(GREEN, LEDMode.OFF)
            ctrlLED(YELLOW, LEDMode.OFF)
            exit(0)
        else:
            print("输入命令无法识别")
            ctrlLED(YELLOW, LEDMode.BLINK)


def main():
    # acquire()
    pass


if __name__ == '__main__':
    main()

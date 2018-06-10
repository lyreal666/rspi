#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import RPi.GPIO as GPIO
from src.globals import GREEN, YELLOW
from src.acquireInput_prod import ctrlLED, LEDMode

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''

# 两个LED灯
global GREEN
global YELLOW


def LEDConfig():
    r"""
    配置LED
    :return:
    """
    global GREEN
    global YELLOW
    GREEN = 6
    YELLOW = 18

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)

    ctrlLED(GREEN, LEDMode.ALWAYS)
    ctrlLED(YELLOW, LEDMode.OFF)


LEDConfig()


def main():
    pass


if __name__ == '__main__':
    main()

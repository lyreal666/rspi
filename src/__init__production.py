#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import RPi.GPIO as GPIO
from src.globalVariables import GREEN, YELLOW
from src.acquireInput_production import ctrlLED, LEDMode

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''



def LEDConfig():
    r"""
    配置LED
    :return:
    """
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

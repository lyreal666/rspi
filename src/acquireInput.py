#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging


logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def acquire(instructions):
    while True:
        instruction = input("输入命令: ")
        if instruction.strip() == "":
            instructions["RECD2PLAY"]()
        elif instruction.lower().strip() == "q":
            exit(0)
        else:
            print("输入命令无法识别")


def main():
    acquire()


if __name__ == '__main__':
    main()

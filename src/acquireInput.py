#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import platform
from .voiceinteraction.voicechat import chat_once

__author__ = 'LY'

'''
    
'''


def acquire():
    while True:
        instruction = input("输入命令: ")
        if instruction.strip() == "":
            chat_once()
        elif instruction.lower().strip() == "ps":
            if platform.platform().split('-')[0] == "Linux":
                from .cameraMonitor.surveillance import photograph
                photograph(20)
        elif instruction.lower().strip() == "q":
            exit(0)
        else:
            print("输入命令无法识别")


if __name__ == '__main__':
    acquire()

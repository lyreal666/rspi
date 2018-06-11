#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from src.voiceinteraction.voicechat import chat_once
from utils.voice import play_mp3
from src.acquireInput import acquire


__author__ = 'LY'

'''
    
'''


def test_chat():
    chat_once()


def main():
    play_mp3(r"F:\codingSpace\Python\rspi\static\audios\程序启动语音.mp3")
    acquire()


if __name__ == '__main__':
    main()

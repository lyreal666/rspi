#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from pydub import AudioSegment


logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def cut_head():
    thirty_seconds = 30 * 1000
    audio = AudioSegment.from_file("../../output/music/b.mp3", "mp3")
    first_10_seconds = audio[:thirty_seconds]
    first_10_seconds.export("../../output/dubs/dubTest.mp3", format="mp3")


def main():
    cut_head()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from src.voiceinteraction.requestmusic import request_music

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


keywords_map = {
    ".*?点.*?歌?.*": {
        "prompt": "点歌.mp3",
        "func": request_music
    }
}



def main():
    pass


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from src.record import recode
from src.au_to_text import voice_to_text

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def main():
    file_name = "test"
    recode(5, file_name)
    print(voice_to_text("../output/audios/%s.wav" % file_name))


if __name__ == '__main__':
    main()

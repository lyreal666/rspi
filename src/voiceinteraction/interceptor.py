#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import re
from src.voiceinteraction.keywords import keywords_map

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''

for keyword in keywords_map:
    pattern = re.compile(r"%s" % keyword)
    keywords_map[keyword]["pattern"] = pattern


def intercept(words):
    for key in keywords_map:
        rs = keywords_map[key]["pattern"].match(words)
        if rs:
            keywords_map[key]["func"]()
            print("开始%s" % key)
            return False
    return True



def main():
    pass


if __name__ == '__main__':
    main()

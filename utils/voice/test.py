#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def test():
    with open("../../configs/baidu_yuyin.json", "r") as fr:
        print(fr.read())



if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from src.record import recode
from src.au_to_text import voice_to_text
from src.jasmine import say2xiaoMei
from src.tuling import say2tutu

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def test_chat():
    start_word = "我艹尼玛"
    for times in range(20):
        debug("小美说: %s", start_word)
        tutu_ret = say2tutu(start_word)
        debug("tutu说: %s", tutu_ret)
        start_word = say2xiaoMei(tutu_ret)


def test_recode2text():
    recode_path = recode(3)
    print("录音转文字: ", voice_to_text(recode_path))


def main():
    test_recode2text()


if __name__ == '__main__':
    main()

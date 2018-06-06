#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from src.voiceinteraction.voicechat import chat_once
from src.acquireInput import acquire
from utils.tpath import resolve
logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def test_chat():
    chat_once()


def main():
    # test_chat()
    acquire({
        "RECD2PLAY": chat_once
    })


if __name__ == '__main__':
    main()

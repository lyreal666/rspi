#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
from urllib import request
from urllib.parse import quote
from src.voicechat.au_to_text import get_token
import hashlib

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
   语音合成
'''


def get_file_name(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    file_name = md5.hexdigest()
    return file_name


def text_to_voice(text):
    url = "https://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
    cuid = "120.78.173.232"
    text = quote(text)
    file_name = get_file_name(text)
    token = get_token()
    url = url % (text, cuid, token)
    with request.urlopen(url) as ug:
        data = ug.read()
        file_name = save_voice(data, file_name)
        return file_name


def save_voice(data, file_name):
    with open("../output/audios/%s.mp3" % file_name, "wb") as fw:
        fw.write(data)
    return "../output/audios/%s.mp3" % file_name


def main():
    text = "自我介绍"
    print(get_file_name(text))
    data = text_to_voice(text)
    save_voice(data, "zwjs")


if __name__ == '__main__':
    main()

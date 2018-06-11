#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import json
import os
from urllib import request
from urllib.parse import quote
from utils.voice.au_to_text import get_token
from utils.voice.play_audio import play_mp3
from utils.tpath import resolve
import hashlib

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
   语音合成
'''


def get_file_path(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    file_name = md5.hexdigest()
    return resolve(__file__, "../../output/audios/%s.mp3" % file_name)


def text_to_voice(text):
    url = "https://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
    cuid = "120.78.173.232"
    text = quote(text)
    token = get_token()
    url = url % (text, cuid, token)
    with request.urlopen(url) as ug:
        data = ug.read()
        return data


def text2audio(text, file_path=""):
    data = text_to_voice(text)
    if file_path.strip() == '':

        file_path = get_file_path(text)
    with open(file_path, "wb") as fw:
        fw.write(data)
    return file_path


def prompt2audio():
    with open(resolve(__file__, "../../configs/prompt.json"), "r", encoding="utf-8") as fr:
        prompts = json.load(fr)
        for keyword in prompts.keys():
            print(keyword)
            if keyword not in [file_name[0: -4] for file_name in os.listdir(r"F:\codingSpace\Python\rspi\static\audios")]:
                path = text2audio(prompts[keyword], resolve(__file__, "../../static/audios/%s.mp3" % keyword))
                play_mp3(path)


def main():
    prompt2audio()


if __name__ == '__main__':
    main()

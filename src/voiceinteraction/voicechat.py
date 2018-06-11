#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import os
from utils.voice import text2audio, recode, play_mp3, voice_to_text, say2xiaoMei
from .interceptor import intercept
from utils.tpath import resolve

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''

'''


def clear_audios(max_count=10):
    clear_dir = resolve(__file__, "../../output/audios/")
    files = [os.path.join(clear_dir, f) for f in os.listdir(clear_dir)]
    files.sort(key=lambda x: os.path.getctime(x))

    if len(files) >= max_count:
        for file in files[0: 10]:
            try:
                os.remove(file)
            except PermissionError as pe:
                debug(f"文件使用中, 文件: {file}")
            except FileNotFoundError as fnfe:
                debug(f"文件找不到: {file}")


def chat_once():
    recode_path = recode(5)
    translation_text = voice_to_text(recode_path)
    if translation_text is None:
        play_mp3(r"F:\codingSpace\Python\rspi\static\audios\语音解析失败.mp3")
        return
    if intercept(translation_text):
        xiaoMei_ret = say2xiaoMei(translation_text)
        audio_path = text2audio(xiaoMei_ret)
        play_mp3(audio_path)
        # play_mplayer(audio_path)
        clear_audios()





def main():
    pass


if __name__ == '__main__':
    main()

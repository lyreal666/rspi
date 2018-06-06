#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import os
from utils.voice.record import recode
from utils.voice.au_to_text import voice_to_text
from utils.voice.text_to_au import text2audio
from utils.voice.jasmine import say2xiaoMei
from utils.voice.play_audio import play_mplayer, play_mp3
from src.voiceinteraction.interceptor import intercept
from src.acquireInput import acquire

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''

'''


def clear_audios(max_count=10):
    clear_dir = "../output/audios/"
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
    if intercept(translation_text):
        xiaoMei_ret = say2xiaoMei(translation_text)
        audio_path = text2audio(xiaoMei_ret)
        play_mp3(audio_path)
        # play_mplayer(audio_path)
        clear_audios()



def test_all():
    acquire({
        'RECD2PLAY': chat_once()
    })


def main():
    test_all()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import os
from src.voicechat.record import recode
from src.voicechat.au_to_text import voice_to_text
from src.voicechat.text_to_au import text_to_voice
from src.voicechat.jasmine import say2xiaoMei
from src.voicechat.tuling import say2tutu
from src.voicechat.play_audio import play_mp3
from src.acquireInput import acquire

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def clear_audios(max_count = 10):
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


def chat_once():
    recode_path = recode(5)
    translation_text = voice_to_text(recode_path)
    xiaoMei_ret = say2xiaoMei(translation_text)
    audio_path = text_to_voice(xiaoMei_ret)
    play_mp3(audio_path)
    clear_audios()


def test_all():
    acquire({
        'RECD2PLAY': chat_once()
    })


def main():
    # test_chat()
    # test_recode2text()
    # test_recd2play()
    test_all()



if __name__ == '__main__':
    main()

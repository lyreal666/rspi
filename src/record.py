#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import pyaudio
import wave
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000


def recode(seconds):
    r"""
    录音接口
    :param seconds:
    :param file_name:
    :return: 录音文件名
    """
    RECORD_SECONDS = seconds
    WAVE_OUTPUT_FILENAME = "../output/audios/%s.wav" % str(datetime.now().timestamp())

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    debug("(***************start recording*********************")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    debug("*****************done recording******************")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME


def main():
    recode(3)


if __name__ == '__main__':
    main()

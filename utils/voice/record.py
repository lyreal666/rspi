#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import logging
import subprocess
from time import sleep
import platform
import wave
from datetime import datetime
from utils.tpath import resolve

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''




def recode(seconds):
    r"""
    录音接口
    :param seconds:
    :param file_name:
    :return: 录音文件名
    """
    system = platform.platform().split('-')[0]
    if system == "Windows":
        import pyaudio
        CHUNK = 512
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = seconds
        WAVE_OUTPUT_FILENAME = resolve(__file__, "../../output/audios/%s.wav" % str(datetime.now().timestamp()))

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        debug(f"***************start recording {seconds}秒*********************")

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
    elif system == "Linux":
        WAVE_OUTPUT_FILENAME = resolve(__file__, "../../output/audios/%s.wav" % str(datetime.now().timestamp()))
        shell_script = " ".join(['arecord ', '-r', str(44100), '-f',
                               'S16_LE', '-c', '1', '-d', str(seconds), '-t', 'wav',
                               '-D', 'hw:1,0', WAVE_OUTPUT_FILENAME])
        print(shell_script)
        subprocess.run(shell_script, shell=True, check=True, stdout=subprocess.PIPE)

        return WAVE_OUTPUT_FILENAME


def main():

    pass


if __name__ == '__main__':
    main()

"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import pygame
import time
import threading
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug


def play_wav(audio_path):
    CHUNK = 1024

    wf = wave.open(audio_path, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


def play_mp3_task(path, duration):
    VOLUME = 0.8
    DURATION = duration

    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(VOLUME)
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(loops=1, start=0.0)
        time.sleep(DURATION)


def play_mp3(path, duration=10):
    try:
        t = threading.Thread(target=play_mp3_task, args=(path, duration), name="play_mp3")
        t.start()
    except Exception as e:
        debug("Path； %s" % path)
        debug(e)


def play_mplayer(path):
    r = subprocess.call(["mplayer", path])
    return r


if __name__ == "__main__":
    play_mp3("../../output/audios/zwjs.mp3")
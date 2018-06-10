"""PyAudio Example: Play a WAVE file."""

from time import sleep
import platform
import threading
import logging
import subprocess
# import pyaudio
# import wave

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug


# def play_wav(audio_path):
#     CHUNK = 1024
#
#     wf = wave.open(audio_path, 'rb')
#
#     p = pyaudio.PyAudio()
#
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
#
#     data = wf.readframes(CHUNK)
#
#     while data != '':
#         stream.write(data)
#         data = wf.readframes(CHUNK)
#
#     stream.stop_stream()
#     stream.close()
#
#     p.terminate()


def _play_mp3_task(path, duration):
    from pygame import mixer
    VOLUME = 0.8
    DURATION = duration

    mixer.init()
    mixer.music.load(path)
    mixer.music.set_volume(VOLUME)
    if not mixer.music.get_busy():
        mixer.music.play(loops=1, start=0.0)
        sleep(DURATION)


def play_mplayer(path):
    r = subprocess.call(["mplayer", path])
    return r


def play_mp3(path, duration=10):
    if platform.platform().split('-')[0] == "Windows":
        try:
            t = threading.Thread(target=_play_mp3_task, args=(path, duration), name="play_mp3")
            t.start()
        except Exception as e:
            debug("Path； %s" % path)
            debug(e)
    elif platform.platform().split('-')[0] == "Linux":
        play_mplayer(path)


if __name__ == "__main__":
    play_mp3("../../output/audios/zwjs.mp3")
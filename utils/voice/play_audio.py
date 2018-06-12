"""PyAudio Example: Play a WAVE file."""

from time import sleep
from os.path import normpath
import platform
import threading
import logging
import subprocess
from pydub import AudioSegment

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

# import pyaudio
# import wave

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


def _play_mp3_task(mixer, path, duration):
    mixer.music.load(path)
    mixer.music.set_volume(0.8)
    while True:
        if not mixer.music.get_busy():
            mixer.music.play(loops=1, start=0.0)
            sleep(duration)
            break
        else:
            pass


def play_mplayer(path):
    subprocess.run(["mplayer", path])


def play_mp3(path):
    ops = platform.platform().split('-')[0]
    if ops == "Windows":
        sound = AudioSegment.from_mp3(path)
        duration = len(sound)
        from pygame import mixer
        mixer.init()
        try:
            t = threading.Thread(target=_play_mp3_task, args=(mixer, path, duration), name="play_mp3")
            t.start()
        except Exception as e:
            debug("Path； %s" % path)
            debug(e)
    elif ops == "Linux":
        path = normpath("/home/pi/projects/rspi/" + path.replace(r"F:\codingSpace\Python\rspi", '')[1:])
        path = path.replace("\\", '/')
        print("播放音乐路径: %s" % path)
        print("抱歉该树莓派音频接口坏了》。。")
        return
        play_mplayer(path)


if __name__ == "__main__":
    play_mp3(r"F:\codingSpace\Python\rspi\static\audios\a.mp3")